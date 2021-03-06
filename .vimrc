set nocompatible              " be iMproved, required
filetype off                  " required

" Plugins {{{
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-repeat'
Plugin 'tpope/vim-fugitive'
Plugin 'tpope/vim-unimpaired'
Plugin 'tpope/vim-surround'
Plugin 'scrooloose/syntastic'
Plugin 'scrooloose/nerdcommenter'
Plugin 'scrooloose/nerdtree'
Plugin 'ctrlpvim/ctrlp.vim'
Plugin 'davidhalter/jedi-vim'
Plugin 'nakamuray/jedi-rpc.vim'
Plugin 'rking/ag.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'altercation/vim-colors-solarized'
Plugin 'fisadev/vim-isort'
Plugin 'nvie/vim-flake8'
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'
Plugin 'easymotion/vim-easymotion'
Plugin 'majutsushi/tagbar'
Plugin 'wikitopian/hardmode'
Plugin 'FooSoft/vim-argwrap'
" Plugin 'kchmck/vim-coffee-script'
" Plugin 'chase/vim-ansible-yaml'
" Plugin 'derekwyatt/vim-scala'
" Plugin 'mjbrownie/pythoncomplete.vim'
" plugin from http://vim-scripts.org/vim/scripts.html
"Plugin 'L9'
" Git plugin not hosted on GitHub
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
let mapleader = " "
" let mapleader = "\<Space>"
syntax on
set modelines=0
set number
set ruler
set visualbell
set wildmenu
set wildmode=list:longest,full
set wildignore=*.o,*~,*.pyc
set laststatus=2
set statusline=\ %{HasPaste()}%F%m%r%h\ %w\ \ CWD:\ %r%{getcwd()}%h\ \ \ Line:\ %l\ \ Column:\ %c\ %{fugitive#statusline()}
set statusline=%<%f\ %h%m%r%{fugitive#statusline()}%=%-14.(%l,%c%V%)\ %P
set undofile
set undodir=~/.vim_runtime/temp_dirs/undodir
set noswapfile
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
set timeout timeoutlen=1000 ttimeoutlen=50
set showmode
set showcmd
set autoindent
set smartindent
set wrap
set nolist
set nrformats=
set tags=tags;/
set listchars=tab:▸\ ,trail:·,extends:#,nbsp:·
set diffopt+=vertical
nnoremap j gj
nnoremap k gk
noremap ; :
noremap ;; ;
nnoremap <leader>; ;
" Save with ctrl-s
noremap <silent> <C-S>          :update<CR>
vnoremap <silent> <C-S>         <C-C>:update<CR>
inoremap <silent> <C-S>         <C-O>:update<CR>
" Copy
vnoremap <C-c> "+y
" Cut
vnoremap <C-x> "+d
" Paste
inoremap <C-v> <C-r>+
" }}}
" Whitespace {{{
set textwidth=119
set formatoptions=tcqrn1
set tabstop=4
set shiftwidth=4
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
set background=dark
colorscheme Tomorrow-Night
"
" }}}
" buffers {{{
nmap <leader>l :bnext<CR>
nmap <leader>h :bprevious<CR>
nmap <leader>q :call OpenLast()<CR>

function! OpenLast()
  if bufloaded(bufnr('#'))
    execute "normal! :b# \<BAR> bd #\<CR>"
  else
    execute "normal! :bnext \<BAR> bd #\<CR>"
  endif
endfunction

nmap <leader>bl :ls<CR>
" }}}
" other stuff {{{

" Visual mode pressing * or # searches for the current selection
vnoremap <silent> * :<C-u>call VisualSelection('', '')<CR>/<C-R>=@/<CR><CR>
vnoremap <silent> # :<C-u>call VisualSelection('', '')<CR>?<C-R>=@/<CR><CR>
" noremap <leader>l :set list!<CR> " Toggle tabs and EOL
" Switch CWD to the directory of the open buffer
noremap <leader>cd :cd %:p:h<CR>:pwd<CR>
vnoremap <silent> <leader>r :call VisualSelection('replace', '')<CR>
nnoremap <leader>w <C-w>v<C-w>l
cnoremap w!! w !sudo tee > /dev/null % <CR>L
" open and close quickfix window
nnoremap <C-q> :call <SID>QuickfixToggle()<cr>

let g:quickfix_is_open = 0

function! s:QuickfixToggle()
    if g:quickfix_is_open
        cclose
        let g:quickfix_is_open = 0
        execute g:quickfix_return_to_window . "wincmd w"
    else
        let g:quickfix_return_to_window = winnr()
        copen
        let g:quickfix_is_open = 1
    endif
endfunction

" Easy window navigation
noremap <C-H> <C-W>h
noremap <C-K> <C-W>k
noremap <C-J> <C-W>j
noremap <C-L> <C-W>l
inoremap <C-H> <C-W>h
inoremap <C-K> <C-W>k
inoremap <C-J> <C-W>j
inoremap <C-L> <C-W>l
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

iabbrev @@ # author: Krystian Dowolski (krystian.dowolski@dealavo.com)

au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
" Reselect text that was just pasted with ,v
nnoremap <leader>v V`]
nnoremap , za

" Copy file to buffer
noremap <leader>fa :let @+ = expand("%")<CR>
noremap <leader>ff :let @+ = expand("%:t")<CR>
noremap <leader>fp :let @+ = expand("%:p")<CR>
noremap <leader>fd :let @+ = expand("%:h")<CR>
noremap <leader>fi :let @+ = "from " . substitute(expand("%:r"),"/",".","g") . " import "<CR>

nnoremap <C-n> :set relativenumber!<CR>
" Pull word under cursor into LHS of a substitute
nnoremap <leader>z :%s#\<<C-r>=expand("<cword>")<CR>\>#
nnoremap <leader>W :%s/\s\+$//<CR>:let @/=''<CR>

" nmap <C-l> :redraw!<CR>
" }}}
" Ag config {{{
if executable('ag')
   " Use ag over grep
   set grepprg=ag\ --nogroup\ --nocolor
endif

" Define "Ag" command
" command! -nargs=+ -complete=file -bar Ag silent! grep! <args> | !awk '{ if (length($0) < 100) print }' | cwindow | redraw!
command! -nargs=+ -complete=file -bar Ag silent! grep! <args> | cwindow | redraw!
" command! -nargs=+ -complete=file -bar Ag silent! grep! <args>
vnoremap <leader>a y:grep! <c-r><cr>:cw<cr> 
nnoremap <leader>aa :Ag <c-r><c-w><CR>
nnoremap <leader>af :Ag %:t:r<CR>
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
" Ctrlp config {{{
" Setup some default ignores
let g:ctrlp_custom_ignore = {
            \ 'dir':  '\v[\/](\.(git|hg|svn)|\_site)$',
            \ 'file': '\v\.(exe|so|dll|class|png|jpg|jpeg)$',
            \}

" Use the nearest .git directory as the cwd
" This makes a lot of sense if you are working on a project that is in version
" control. It also supports works with .svn, .hg, .bzr.
let g:ctrlp_working_path_mode = 'r'

" Use a leader instead of the actual named binding
nmap <leader>p :CtrlP<cr>

" Easy bindings for its various modes
nmap <leader>bb :CtrlPBuffer<cr>
nmap <leader>bm :CtrlPMRU<cr>
nmap <leader>bs :CtrlPMixed<cr>
" }}}
" {{{ flake8 config
let g:flake8_show_in_gutter=1
" autocmd BufWritePost *.py call Flake8()
" }}}
" fugitive config {{{
nnoremap <leader>gw :Gwrite!<cr>
nnoremap <leader>gr :Gread<space>
nnoremap <leader>ge :Gedit<space>
nnoremap <leader>gs :Gstatus<cr>
nnoremap <leader>gd :Gremove<cr>
nnoremap <leader>gd :Gdiff<cr>
nnoremap <leader>gm :Gdiff origin/master
nnoremap <leader>ga :Gcommit --amend<cr>
nnoremap <leader>gc :Gcommit<cr>
nnoremap <leader>gv :Gmove<space>
nnoremap gl :diffget //2 <bar> diffupdate<cr>
nnoremap gr :diffget //3 <bar> diffupdate<cr>
nnoremap <leader>gb :Gblame<cr>
nnoremap <leader>go :Gbrowse<cr>

autocmd User fugitive 
  \ if fugitive#buffer().type() =~# '^\%(tree\|blob\)$' |
  \   nnoremap <buffer> .. :edit %:h<CR> |
  \ endif
autocmd BufReadPost fugitive://* set bufhidden=delete

autocmd FilterWritePre * if &diff | setlocal wrap< | endif
" }}}
" NERDTree config {{{
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <leader>m :NERDTreeClose<CR>:NERDTreeFind<CR>
nnoremap <leader>N :NERDTreeClose<CR>

" Store the bookmarks file
let NERDTreeBookmarksFile=expand("$HOME/.vim/NERDTreeBookmarks")

" Show the bookmarks table on startup
let NERDTreeShowBookmarks=1

" Show hidden files, too
let NERDTreeShowFiles=1
let NERDTreeShowHidden=1

" Quit on opening files from the tree
let NERDTreeQuitOnOpen=1

" Highlight the selected entry in the tree
let NERDTreeHighlightCursorline=1

" Use a single click to fold/unfold directories and a double click to open
" files
let NERDTreeMouseMode=2

" Don't display these kinds of files
let NERDTreeIgnore=[ '\.pyc$', '\.pyo$', '\.py\$class$', '\.obj$',
            \ '\.o$', '\.so$', '\.egg$', '^\.git$', '__pycache__', '\.DS_Store' ]

" }}}
" {{{ NERDComment config
let g:NERDSpaceDelims = 1

" Use compact syntax for prettified multi-line comments
let g:NERDCompactSexyComs = 1

" Align line-wise comment delimiters flush left instead of following code indentation
let g:NERDDefaultAlign = 'left'

" Set a language to use its alternate delimiters by default
let g:NERDAltDelims_java = 1

" Add your own custom formats or override the defaults
let g:NERDCustomDelimiters = { 'c': { 'left': '/**','right': '*/' } }

" Allow commenting and inverting empty lines (useful when commenting a region)
let g:NERDCommentEmptyLines = 1

" Enable trimming of trailing whitespace when uncommenting
let g:NERDTrimTrailingWhitespace = 1

nmap <C-_> <Plug>NERDCommenterInvert
vmap <C-_> <Plug>NERDCommenterInvert
" }}}
" ultisnips config {{{
 " Trigger configuration. Do not use <tab> if you use https://github.com/Valloric/YouCompleteMe.
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<c-m>"
let g:UltiSnipsJumpBackwardTrigger="<c-b>"
let g:UltiSnipsListSnippets="lll"
nnoremap <leader>u :UltiSnipsEdit<cr>
"let g:UltiSnipsSnippetDirectories=[".vim/bundle/vim-snippets/UltiSnips"]
let g:UltiSnipsSnippetsDir = "~/.vim/bundle/ultisnips/UltiSnips"

" If you want :UltiSnipsEdit to split your window.
let g:UltiSnipsEditSplit="vertical"
" }}}
" syntastic config {{{
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

let g:syntastic_mode_map = { 'mode': 'passive', 'active_filetypes': [],'passive_filetypes': [] }
nnoremap <F8> :SyntasticCheck<CR>
" :SyntasticToggleMode<CR>
" }}}
" easymotion config {{{
let g:EasyMotion_do_mapping = 0 " Disable default mappings

" Jump to anywhere you want with minimal keystrokes, with just one key binding.
" `s{char}{label}`
" nmap s <Plug>(easymotion-overwin-f)
" or
" `s{char}{char}{label}`
" Need one more keystroke, but on average, it may be more comfortable.

" Turn on case insensitive feature
let g:EasyMotion_smartcase = 1

" JK motions: Line motions
map <Leader>j <Plug>(easymotion-j)
map <Leader>k <Plug>(easymotion-k)
" }}}
" argwrap config {{{
let g:argwrap_tail_comma = 1
nnoremap <silent> <leader>o :ArgWrap<CR>
" }}}
" tagbar config {{{
nmap <F9> :TagbarToggle<CR>
" }}}
" syntastic config {{{
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

let g:syntastic_mode_map = { 'mode': 'passive', 'active_filetypes': [],'passive_filetypes': [] }
nnoremap <F8> :SyntasticCheck<CR>
" :SyntasticToggleMode<CR>
" }}}
" easymotion config {{{
let g:EasyMotion_do_mapping = 0 " Disable default mappings

" Jump to anywhere you want with minimal keystrokes, with just one key binding.
" `s{char}{label}`
" nmap s <Plug>(easymotion-overwin-f)
" or
" `s{char}{char}{label}`
" Need one more keystroke, but on average, it may be more comfortable.

" Turn on case insensitive feature
let g:EasyMotion_smartcase = 1

" JK motions: Line motions
map <Leader>j <Plug>(easymotion-j)
map <Leader>k <Plug>(easymotion-k)
" }}}
" argwrap config {{{
let g:argwrap_tail_comma = 1
nnoremap <silent> <leader>o :ArgWrap<CR>
" }}}
" tagbar config {{{
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
" smooth scrolling {{{
set mouse=a
nnoremap <C-e> 2<C-e>
nnoremap <C-y> 2<C-y>
map <ScrollWheelUp> <C-Y>
map <ScrollWheelDown> <C-E>

function! SmoothScroll(up)
    if a:up
        let scrollaction=""
    else
        let scrollaction=""
    endif
    exec "normal! " . scrollaction
    redraw
    let counter=1
    while counter<&scroll
        let counter+=1
        sleep 10m
        redraw
        exec "normal! " . scrollaction
    endwhile
endfunction

nnoremap <C-u> :call SmoothScroll(1)<Enter>
nnoremap <C-d> :call SmoothScroll(0)<Enter>
inoremap <C-U> <Esc>:call SmoothScroll(1)<Enter>i
inoremap <C-D> <Esc>:call SmoothScroll(0)<Enter>i

" }}}
" to help learn new macros {{{
inoremap <ESC> <nop>
nnoremap <up> <nop>
nnoremap <down> <nop>
nnoremap <left> <nop>
nnoremap <right> <nop>
" cnoremap w echo("it wont work")
" }}}
" {{{ autoread
function! WatchForChanges(bufname, ...)
  " Figure out which options are in effect
  if a:bufname == '*'
    let id = 'WatchForChanges'.'AnyBuffer'
    " If you try to do checktime *, you'll get E93: More than one match for * is given
    let bufspec = ''
  else
    if bufnr(a:bufname) == -1
      echoerr "Buffer " . a:bufname . " doesn't exist"
      return
    end
    let id = 'WatchForChanges'.bufnr(a:bufname)
    let bufspec = a:bufname
  end
  if len(a:000) == 0
    let options = {}
  else
    if type(a:1) == type({})
      let options = a:1
    else
      echoerr "Argument must be a Dict"
    end
  end
  let autoread    = has_key(options, 'autoread')    ? options['autoread']    : 0
  let toggle      = has_key(options, 'toggle')      ? options['toggle']      : 0
  let disable     = has_key(options, 'disable')     ? options['disable']     : 0
  let more_events = has_key(options, 'more_events') ? options['more_events'] : 0 "WARNING changed from 1
  let while_in_this_buffer_only = has_key(options, 'while_in_this_buffer_only') ? options['while_in_this_buffer_only'] : 0
  if while_in_this_buffer_only
    let event_bufspec = a:bufname
  else
    let event_bufspec = '*'
  end
  let reg_saved = @"
  "let autoread_saved = &autoread
  let msg = "\n"
  " Check to see if the autocommand already exists
  redir @"
    silent! exec 'au '.id
  redir END
  let l:defined = (@" !~ 'E216: No such group or event:')
  " If not yet defined...
  if !l:defined
    if l:autoread
      let msg = msg . 'Autoread enabled - '
      if a:bufname == '*'
        set autoread
      else
        setlocal autoread
      end
    end
    silent! exec 'augroup '.id
      if a:bufname != '*'
        "exec "au BufDelete    ".a:bufname . " :silent! au! ".id . " | silent! augroup! ".id
        "exec "au BufDelete    ".a:bufname . " :echomsg 'Removing autocommands for ".id."' | au! ".id . " | augroup! ".id
        exec "au BufDelete    ".a:bufname . " execute 'au! ".id."' | execute 'augroup! ".id."'"
      end
        exec "au BufEnter     ".event_bufspec . " :checktime ".bufspec
        exec "au CursorHold   ".event_bufspec . " :checktime ".bufspec
        exec "au CursorHoldI  ".event_bufspec . " :checktime ".bufspec
      " The following events might slow things down so we provide a way to disable them...
      " vim docs warn:
      "   Careful: Don't do anything that the user does
      "   not expect or that is slow.
      if more_events
        exec "au CursorMoved  ".event_bufspec . " :checktime ".bufspec
        exec "au CursorMovedI ".event_bufspec . " :checktime ".bufspec
      end
    augroup END
    let msg = msg . 'Now watching ' . bufspec . ' for external updates...'
  end
  " If they want to disable it, or it is defined and they want to toggle it,
  if l:disable || (l:toggle && l:defined)
    if l:autoread
      let msg = msg . 'Autoread disabled - '
      if a:bufname == '*'
        set noautoread
      else
        setlocal noautoread
      end
    end
    " Using an autogroup allows us to remove it easily with the following
    " command. If we do not use an autogroup, we cannot remove this
    " single :checktime command
    " augroup! checkforupdates
    silent! exec 'au! '.id
    silent! exec 'augroup! '.id
    let msg = msg . 'No longer watching ' . bufspec . ' for external updates.'
  elseif l:defined
    let msg = msg . 'Already watching ' . bufspec . ' for external updates'
  end
"  echo msg
  let @"=reg_saved
endfunction

let autoreadargs={'autoread':1}
execute WatchForChanges("*",autoreadargs)
" }}}
" Pulse {{{
" nnoremap n n:call PulseCursorLine()<cr>
" nnoremap N N:call PulseCursorLine()<cr>

function! PulseCursorLine()
    setlocal cursorline

    redir => old_hi
        silent execute 'hi CursorLine'
    redir END
    let old_hi = split(old_hi, '\n')[0]
    let old_hi = substitute(old_hi, 'xxx', '', '')

    hi CursorLine guibg=#3a3a3a
    redraw
    sleep 14m

    hi CursorLine guibg=#4a4a4a
    redraw
    sleep 10m

    hi CursorLine guibg=#3a3a3a
    redraw
    sleep 14m

    hi CursorLine guibg=#2a2a2a
    redraw
    sleep 10m

    execute 'hi ' . old_hi
    setlocal nocursorline
endfunction
" }}}
" WORK {{{
set noexpandtab
" }}}
