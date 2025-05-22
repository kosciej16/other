local success, Job = pcall(require, "plenary.job")
if not success then
	print("Failed to load plenary.job")
else
	-- Create a new job to run the `echo` command
	Job:new({
		command = "echo",
		args = { "Hello from Plenary!" },
		on_exit = function(j, return_val)
			if return_val == 0 then
				print(table.concat(j:result(), "\n"))
			else
				print("Job failed with return value", return_val)
			end
		end,
	}):sync()
end
