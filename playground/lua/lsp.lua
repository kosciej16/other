local M = {}

local Job = require("plenary.job")
local Path = require("plenary.path")

-- local warn = require("warn").warn
-- local open_file = require("pytrize.jump.util").open_file

local function normal(cmd)
    vim.cmd(string.format("normal! %s", cmd))
end

local function get_word_under_cursor()
    local savereg = vim.fn.getreginfo('"')
    normal("yiw")
    local word = vim.fn.getreg('"')
    vim.fn.setreg('"', savereg)
    return word
end

local function parse_raw_fixture_output(cwd, lines)
    local fixtures = {}
    local pattern = "^([%w_]*) .*%-%- (%S*):(%d*)$"
    for _, line in ipairs(lines) do
        local i, _, fixture, file, linenr = string.find(line, pattern)
        if i ~= nil then
            fixtures[fixture] = {
                file = cwd / file,
                linenr = tonumber(linenr),
            }
        end
    end
    return fixtures
end

local function get_cwd()
    return Path:new(vim.api.nvim_buf_get_name(0)):parent()
end

local function lookup_fixtures(callback)
    local cwd = get_cwd()
    Job:new({
        -- command = "ls",
        command = "pytest",
        args = { "--fixtures", "-v" },
        -- command = "/home/kosciej/repos/itsg/local/starfish/.direnv/python-3.12/bin/python",
        -- args = { "-m", "pytest", "--fixtures", "-v" },
        cwd = tostring(cwd),
        -- cwd = "/home/kosciej/repos/itsg/local/starfish/",
        on_exit = vim.schedule_wrap(function(j, return_val)
            if return_val == 0 then
                local fixtures = parse_raw_fixture_output(cwd, j:result())
                callback(fixtures)
                -- else
                -- 	warn(string.format("failed to query fixtures: %s", table.concat(j:result(), "\n")))
            end
        end),
    }):sync(35000)
end

M.to_declaration = function()
    local fixture = get_word_under_cursor()
    lookup_fixtures(function(fixtures)
        local fixture_location = fixtures[fixture]
        if fixture_location == nil then
            warn(string.format('fixture "%s" not found', fixture))
        else
            local file = fixture_location.file
            local linenr = fixture_location.linenr
            -- open_file(tostring(file))
            vim.api.nvim_command("edit " .. file)
            vim.api.nvim_win_set_cursor(0, { linenr, 0 })
            vim.fn.search(fixture)
        end
    end)
end

function print_param(param)
    for k, v in pairs(param) do
        print(k, v)
    end
end

vim.cmd("e /home/kosciej/tmp/som.py")
function test_me()
    local lspconfig = require("lspconfig")
    -- local servers = lspconfig.util.available_servers()
    local clients = vim.lsp.get_active_clients()
    -- local clients = vim.lsp.buf_get_clients(0) -- Gets clients for the currently active buffer

    for i, client in ipairs(clients) do
        local lines = vim.split(vim.inspect(client.server_capabilities), "\n")
        -- for _, line in ipairs(lines) do
        --     print(line)
        -- end

        local file = io.open(string.format("lsp_capabilities_%s.json", client.name), "w")
        if file then
            -- Convert table to string with vim.inspect
            local output = vim.inspect(client)
            file:write(output)
            file:close()
        else
            print("Failed to open file for writing")
        end
        print(client.name)
        vim.print(client.server_capabilities)
        -- local root_dir = client.config.root_dir or client.config.workspace_folders[1].uri
        -- print("LSP Root Directory: " .. root_dir)
    end
end

vim.defer_fn(test_me, 1000) -- Delay for 1000 ms to allow LSP clients to start
-- lookup_fixtures(print_param)
vim.defer_fn(function()
    vim.cmd("qa!")
end, 2000)
