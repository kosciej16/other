function prettyPrintTable(tbl, indent)
	indent = indent or 0
	local toprint = string.rep(" ", indent) .. "{\n"
	indent = indent + 2
	for k, v in pairs(tbl) do
		toprint = toprint .. string.rep(" ", indent)
		if type(k) == "number" then
			toprint = toprint .. "[" .. k .. "] = "
		elseif type(k) == "string" then
			toprint = toprint .. k .. " = "
		end
		if type(v) == "number" then
			toprint = toprint .. v .. ",\n"
		elseif type(v) == "string" then
			toprint = toprint .. '"' .. v .. '",\n'
		elseif type(v) == "table" then
			toprint = toprint .. prettyPrintTable(v, indent + 2) .. ",\n"
		else
			toprint = toprint .. '"' .. tostring(v) .. '",\n'
		end
	end
	toprint = toprint .. string.rep(" ", indent - 2) .. "}"
	return toprint
end

local function parse_raw_fixture_output(lines)
	local fixtures = {}
	local pattern = "^([^_][%w_]*) .*%-%- (%S*):(%d*)"
	for line in lines do
		local name, path, linenr = line:match(pattern)
		if name ~= nil then
			print(name, path, linenr)
			fixtures[name] = {
				file = path,
				linenr = tonumber(linenr),
			}
		end
	end
	return fixtures
end
local function readf()
	local file = io.open("tmp", "r")
	local c = file:lines()
	res = parse_raw_fixture_output(c)
	-- print(prettyPrintTable(res, 4))
end

readf()
