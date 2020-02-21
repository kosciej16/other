map <leader>rr :!clear && python -m pytest %<CR>
map <leader>rm :!clear && python -m pytest "mojmarker1"<CR>

noremap <leader>pr :!python %<CR>
noremap <leader>pm mt?def<CR>O@pytest.mark.mojmarker1<ESC>'t

" isort {{{
let g:vim_isort_python_version = 'python3'
nnoremap <leader>po :Isort<cr>
" }}}
" auto import {{{
map <leader>pi    mz:ImportName<CR>'z
" }}}
