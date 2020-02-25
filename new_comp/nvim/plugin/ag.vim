if executable('ag')
   " Use ag over grep
   " set grepprg=ag\ --nogroup\ --nocolor\ --path-to-ignore\ ~/.ignore
   set grepprg=ag\ --path-to-ignore\ /home/kosciej/.ignore
   " set grepprg=ag
endif

" Define "Ag" command
" command! -nargs=+ -complete=file -bar Ag silent! grep! <args> | !awk '{ if (length($0) < 100) print }' | cwindow | redraw!
command! -nargs=+ -complete=file -bar Ag  silent! grep! <args> | cwindow | redraw!
" command! -nargs=+ -complete=file -bar Ag silent! grep! <args>
vnoremap <leader>a y:grep! <c-r><cr>:cw<cr>
nnoremap <leader>aa :Ag <c-r><c-w><CR>
nnoremap <leader>af :Ag %:t:r<CR>
nnoremap <leader>aw :Ag <c-r>"<CR>
nnoremap <leader>ae :Ag -a
nnoremap <leader>ar :<c-r>: -a<CR>
nnoremap <leader>an :Ag -l <c-r><c-w><CR>
nnoremap K *N:grep! "\b<c-r><c-w>\b"<cr>:cw<cr>

" Allow quick additions to the spelling dict
" nnoremap <leader>g :spellgood <c-r><c-w>


" bind \ (backward slash) to grep shortcut
nnoremap \ :Ag<SPACE>

let g:ag_working_path_mode="a"
let g:ag_max_line_len = 200
" vnoremap <silent> <leader>a :call VisualSelection('gv', '')<CR>
" map <leader>cc :botright cope<cr>
" map <leader>co ggVGy:tabnew<cr>:set syntax=qf<cr>pgg
" map <leader>n :cn<cr>
" map <leader>p :cp<cr>
" don't wrap results
autocmd FileType qf setlocal nowrap
