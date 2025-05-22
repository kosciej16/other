package.path = package.path .. ";./?.lua;./?/init.lua"

print(package.path)
-- print(package.cpath)

print(gl)
mod = require("config")
print("Module loaded:", mod)

print(gl)
print(gl.param)
local globs = { "~/.config/neomutt/", "~/.config/tmux/", "~/.config/bspwm/", "~/.config/sxhkd/", "~/.aliases/"}
local files = {"a"}

local t = {3, 4, 5}
local concatenation = {1, 2, unpack(t)}
print(concatenation)
for _, g in ipairs(globs) do
    for _, path in ipairs(vim.split(vim.fn.globpath(g, "*"), "\n")) do
        table.insert(files, path)
    end
end
for _, g in ipairs(files) do
    print(g)
end
