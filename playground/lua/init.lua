local plug_path = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
vim.opt.rtp:prepend(plug_path)

require("lazy").setup({
	"nvim-lua/plenary.nvim",
	-- other plugins if necessary
})
