set nocompatible              " be iMproved, required
filetype off                  " required

" Plugins {{{
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'davidhalter/jedi-vim'
Plugin 'ctrlpvim/ctrlp.vim'
Plugin 'rking/ag.vim'
"Plugin 'mileszs/ack.vim'
Plugin 'tpope/vim-surround'
Plugin 'vim-airline/vim-airline'
Plugin 'altercation/vim-colors-solarized'
Plugin 'tpope/vim-repeat'

"Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
"Plugin 'L9'
" Git plugin not hosted on GitHub
"Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
"Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
"Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
"Plugin 'ascenator/L9', {'name': 'newL9'}

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" }}}
" Vimscript file settings ---------------------- {{{
augroup filetype_vim
    autocmd!
    autocmd FileType vim setlocal foldmethod=marker
augroup END
" }}}
" Basic stuff {{{
syntax on
set modelines=0
set number
set ruler
set visualbell
set wildmenu
set wildmode=list:longest
set wildignore=*.o,*~,*.pyc
set laststatus=2
set statusline=\ %{HasPaste()}%F%m%r%h\ %w\ \ CWD:\ %r%{getcwd()}%h\ \ \ Line:\ %l\ \ Column:\ %c
set undofile
set undodir=~/.vim_runtime/temp_dirs/undodir
set autoread
set encoding=utf-8
set whichwrap+=<,>,h,l
set lazyredraw
set foldcolumn=1
set scrolloff=3
set backspace=indent,eol,start
set matchpairs+=<:>
set hidden
set ttyfast
set showmode
set showcmd
set autoindent
set smartindent
set wrap
set nolist
set nrformats=
set listchars=tab:▸\ ,trail:·,extends:#,nbsp:·
nnoremap j gj
nnoremap k gk
map ; :
let mapleader = "\<Space>"
" }}}
" Whitespace {{{
set textwidth=119
set formatoptions=tcqrn1
set tabstop=4
set shiftwidth=2
set softtabstop=8
set expandtab
set smarttab
set noshiftround
" }}}
" Searching {{{
nnoremap / /\v
vnoremap / /\v
set hlsearch
set incsearch
set ignorecase
set smartcase
set showmatch
set gdefault
" }}}
" Color scheme {{{
set t_Co=256
set background=dark
let g:solarized_termcolors=256
let g:solarized_termtrans=1
" put https://raw.github.com/altercation/vim-colors-solarized/master/colors/solarized.vim
" in ~/.vim/colors/ and uncomment:
" colorscheme solarized
"
" }}}
" buffers {{{
nmap <leader>l :bnext<CR>
nmap <leader>h :bprevious<CR>
nmap <leader>q :bp <BAR> bd #<CR>
nmap <leader>bl :ls<CR>
" }}}
" other stuff {{{
let g:jedi#smart_auto_mappings = 0
let g:jedi#completions_enabled = 0

" Visual mode pressing * or # searches for the current selection
vnoremap <silent> * :<C-u>call VisualSelection('', '')<CR>/<C-R>=@/<CR><CR>
vnoremap <silent> # :<C-u>call VisualSelection('', '')<CR>?<C-R>=@/<CR><CR>
noremap <leader>l :set list!<CR> " Toggle tabs and EOL
" Switch CWD to the directory of the open buffer
noremap <leader>cd :cd %:p:h<cr>:pwd<cr>
vnoremap <silent> <leader>r :call VisualSelection('replace', '')<CR>
nnoremap <leader>w <C-w>v<C-w>l
cnoremap w!! w !sudo tee > /dev/null %

" Easy window navigation
noremap <C-H> <C-W>h
noremap <C-K> <C-W>k
noremap <C-J> <C-W>j
noremap <C-L> <C-W>l
inoremap jk <ESC>
inoremap <C-e> <Esc>A
inoremap <C-a> <Esc>I
cnoremap <C-A>		<Home>
cnoremap <C-E>		<End>
nnoremap ' `
nnoremap ` '
nnoremap Y y$
" Edit the vimrc file
nnoremap <silent> <leader>ev :e $MYVIMRC<CR>
nnoremap <silent> <leader>sv :so $MYVIMRC<CR>
" Clears the search register
nnoremap <silent> <leader>/ :nohlsearch<CR>
" Jump to matching pairs easily, with Tab
nnoremap <Tab> %
vnoremap <Tab> %

noremap x "_x
vnoremap p "_dP

iabbrev @@ # author: Krystian Dowolski (krystian.dowolski@dealavo.com)

au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
" Reselect text that was just pasted with ,v
nnoremap <leader>v V`]
" }}}
" Ag config {{{
nnoremap <leader>a :Ag<space>
vnoremap <silent> <leader>a :call VisualSelection('gv', '')<CR>
map <leader>cc :botright cope<cr>
map <leader>co ggVGy:tabnew<cr>:set syntax=qf<cr>pgg
map <leader>n :cn<cr>
map <leader>p :cp<cr>
" }}}
" to help learn new macros {{{
inoremap <ESC> <nop>
nnoremap <up> <nop>
nnoremap <down> <nop>
nnoremap <left> <nop>
nnoremap <right> <nop>
" }}}
" Airline config {{{
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#fnamemod = ':t'
let g:airline#extensions#tabline#buffer_idx_mode = 1

nmap <leader>1 <Plug>AirlineSelectTab1
nmap <leader>2 <Plug>AirlineSelectTab2
nmap <leader>3 <Plug>AirlineSelectTab3
nmap <leader>4 <Plug>AirlineSelectTab4
nmap <leader>5 <Plug>AirlineSelectTab5
nmap <leader>6 <Plug>AirlineSelectTab6
nmap <leader>7 <Plug>AirlineSelectTab7
nmap <leader>8 <Plug>AirlineSelectTab8
nmap <leader>9 <Plug>AirlineSelectTab9
" }}}
" autopaste {{{
let &t_SI .= "\<Esc>[?2004h"
let &t_EI .= "\<Esc>[?2004l"

inoremap <special> <expr> <Esc>[200~ XTermPasteBegin()

function! XTermPasteBegin()
  set pastetoggle=<Esc>[201~
  set paste
  return ""
endfunction
" }}}
" functions {{{
function! HasPaste()
    if &paste
        return 'PASTE MODE  '
    endif
    return ''
endfunction

function! CmdLine(str)
    exe "menu Foo.Bar :" . a:str
    emenu Foo.Bar
    unmenu Foo
endfunction 

function! VisualSelection(direction, extra_filter) range
    let l:saved_reg = @"
    execute "normal! vgvy"

    let l:pattern = escape(@", '\\/.*$^~[]')
    let l:pattern = substitute(l:pattern, "\n$", "", "")

    if a:direction == 'gv'
        call CmdLine("Ag \"" . l:pattern . "\" " )
    elseif a:direction == 'replace'
        call CmdLine("%s" . '/'. l:pattern . '/')
    endif

    let @/ = l:pattern
    let @" = l:saved_reg
endfunction
" }}}


