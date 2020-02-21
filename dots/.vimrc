set nocompatible              " be iMproved, required
filetype off                  " required

" Plugins {{{
call plug#begin('~/.config/nvim/bundle')

" Plug 'airblade/vim-gitgutter'
Plug 'alfredodeza/pytest.vim'
Plug 'altercation/vim-colors-solarized'
" Plug 'autozimu/LanguageClient-neovim', { 'branch': 'next', 'do': 'bash install.sh' }
" Plug 'chrisbra/Colorizer'
" Plug 'christoomey/vim-tmux-navigator'
Plug 'codegram/vim-codereview'
Plug 'junkblocker/patchreview-vim'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'davidhalter/jedi-vim'
" Plug 'direnv/direnv.vim'
Plug 'easymotion/vim-easymotion'
" Plug 'edkolev/tmuxline.vim'
" Plug 'ervandew/supertab'
" Plug 'fatih/vim-go'
Plug 'fisadev/vim-isort'
Plug 'godlygeek/tabular'
Plug 'hashivim/vim-terraform'
Plug 'honza/vim-snippets'
" Plug 'janko-m/vim-test'
" Plug 'janko/vim-test'
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim'
" Plug 'junegunn/goyo.vim'
" Plug 'junegunn/gv.vim'
" Plug 'junegunn/limelight.vim'
" Plug 'junegunn/vim-emoji'
" Plug 'junegunn/vim-peekaboo'
" Plug 'justinmk/vim-dirvish'
" Plug 'justinmk/vim-sneak'
" Plug 'kana/vim-textobj-user'
" Plug 'kevinhui/vim-docker-tools'
" Plug 'kshenoy/vim-signature'
Plug 'lervag/vimtex'
" Plug 'ludovicchabant/vim-gutentags'
Plug 'majutsushi/tagbar'
" Plug 'mattn/emmet-vim'
" Plug 'mattn/vim-textobj-url'
Plug 'mbbill/undotree'
Plug 'mileszs/ack.vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'neomake/neomake'
" Plug 'rafi/awesome-vim-colorschemes'
" Plug 'rizzatti/dash.vim'
Plug 'rking/ag.vim'
Plug 'scrooloose/nerdcommenter'
Plug 'scrooloose/nerdtree'
" Plug 'sheerun/vim-polyglot'
" Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'SirVer/ultisnips'
" Plug 'sodapopcan/vim-twiggy'
Plug 'tfnico/vim-gradle'
" Plug 'tmux-plugins/vim-tmux-focus-events'
Plug 'tpope/vim-abolish'
" Plug 'tpope/vim-commentary'
" Plug 'tpope/vim-cucumber'
" Plug 'tpope/vim-dispatch'
" Plug 'tpope/vim-eunuch'
Plug 'tpope/vim-fugitive'
" Plug 'tpope/vim-obsession'
" Plug 'tpope/vim-projectionist'
Plug 'tpope/vim-repeat'
" Plug 'tpope/vim-rhubarb'
Plug 'tpope/vim-rsi'
" Plug 'tpope/vim-sensible'
Plug 'tpope/vim-surround'
Plug 'tpope/vim-unimpaired'
Plug 'tpope/vim-rhubarb'

Plug 'vim-airline/vim-airline'
Plug 'FooSoft/vim-argwrap'
" Plug 'vim-airline/vim-airline-themes'
" Plug 'w0rp/ale'
" Plug 'wellle/targets.vim'

" Plug 'inside/vim-search-pulse'
" Plug 'dense-analysis/ale'
"
Plug 'mgedmin/python-imports.vim'
Plug 'lambdalisue/suda.vim'
Plug 'tell-k/vim-autoflake'
Plug 'vimwiki/vimwiki'
Plug 'rhysd/clever-f.vim'

call plug#end()
filetype plugin indent on    " required
" }}}
"
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
set undodir=~/.config/nvim/undodir
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
map ; :
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
vnoremap <leader>p "_dP
" let g:deoplete#enable_at_startup = 1
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
" noremap <leader>cd :cd %:p:h<CR>:pwd<CR>
vnoremap <silent> <leader>r :call VisualSelection('replace', '')<CR>
nnoremap <leader>w <C-w>v<C-w>l
cnoremap w!! w suda://%<CR>
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

noremap <leader>pj :%!python -m json.tool<CR>

cnoremap <C-P> <Up>
cnoremap <C-N> <Down>
inoremap <C-k> <C-p>
inoremap <C-j> <C-n>


" }}}
" Easy window navigation {{{
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
" Clears the search register
nnoremap <silent> <leader>/ :nohlsearch<CR>

iabbrev @@ # author: Krystian Dowolski (krystian.dowolski@dealavo.com)

au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
" Reselect text that was just pasted with ,v
nnoremap gv `[V`]
nnoremap , za

" Copy file to buffer
noremap <leader>ff :let @+ = expand("%:p")<CR>
noremap <leader>fn :let @+ = expand("%:t")<CR>
noremap <leader>fd :let @+ = expand("%:h")<CR>

nnoremap <C-n> :set relativenumber!
" Pull word under cursor into LHS of a substitute
nnoremap <leader>z :%s#\<<C-r>=expand("<cword>")<CR>\>#
nnoremap <leader>W :%s/\s\+$//<CR>:let @/=''<CR>

" nmap <C-l> :redraw!<CR>
" }}}
" {{{ Open files
nnoremap <silent> <leader>ev :e $MYVIMRC<CR>
nnoremap <silent> <leader>et :e /tmp/som.py<CR>
nnoremap <silent> <leader>ep :e ~/.config/nvim/ftplugin/python/python.vim<CR>
nnoremap <silent> <leader>ec :e ~/.config/nvim/coc-settings.json<CR>
nnoremap <silent> <leader>ei :e ~/.config/nvim/bundle/python-imports.vim/myimports.cfg<CR>
nnoremap <silent> <leader>e3 :e ~/.config/i3/config<CR>
nnoremap <silent> <leader>eb :e ~/.config/i3/i3blocks.conf<CR>
nnoremap <silent> <leader>el :e ~/repos/other/new_comp/steps<CR>
nnoremap <silent> <leader>eg :e ~/.gitconfig<CR>
nnoremap <silent> <leader>ek :e ~/.config/khal/config<CR>
nnoremap <silent> <leader>ek :e ~/.config/khal/config<CR>
nnoremap <silent> <leader>es :so $MYVIMRC<CR>
nnoremap <silent> <leader>eq :e ~/.config/qutebrowser/config.py<CR>
" }}}
" Ag config {{{
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
            \ 'dir':  '\v[\/](\.(git|hg|svn)|\_site|venv)$',
            \ 'file': '\v\.(exe|so|dll|class|png|jpg|jpeg|egg)$',
            \}

" Use the nearest .git directory as the cwd
" This makes a lot of sense if you are working on a project that is in version
" control. It also supports works with .svn, .hg, .bzr.
let g:ctrlp_working_path_mode = ''

" Use a leader instead of the actual named binding
" nmap <leader>p :CtrlP<cr>

" Easy bindings for its various modes
nmap <leader>bb :CtrlPBuffer<cr>
nmap <leader>bm :CtrlPMRU<cr>
nmap <leader>bs :CtrlPMixed<cr>

set maxmempattern=10000
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
nnoremap <leader>gff :Gdiff<cr>
nnoremap <leader>gfm :Gdiff origin/master
nnoremap <leader>ga :Gcommit --amend --no-edit<cr>
nnoremap <leader>gc :Gcommit<cr>
nnoremap <leader>gv :Gmove<space>
nnoremap <leader>gu :Git add -u<cr>
nnoremap <leader>gq :Git add -u<cr>:Gcommit --amend --no-edit<cr>:Git push -f<cr>
nnoremap gl :diffget //2 <bar> diffupdate<cr>
nnoremap gr :diffget //3 <bar> diffupdate<cr>
nnoremap <leader>gb :Gblame<cr>
nnoremap <leader>go :.Gbrowse<cr>
vnoremap <leader>go :Gbrowse<cr>

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

let g:NERDTreeWinSize=50
" }}}
" Coc config {{{
inoremap <silent><expr> <c-space> coc#refresh()

" Use <cr> to confirm completion, `<C-g>u` means break undo chain at current position.
" Coc only does snippet and additional edit on confirm.
inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
" Or use `complete_info` if your vim support it, like:
" inoremap <expr> <cr> complete_info()["selected"] != "-1" ? "\<C-y>" : "\<C-g>u\<CR>"

" Use `[g` and `]g` to navigate diagnostics
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)

" Remap keys for gotos
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  else
    call CocAction('doHover')
  endif
endfunction

" Highlight symbol under cursor on CursorHold
autocmd CursorHold * silent call CocActionAsync('highlight')

" Remap for rename current word
nmap <leader>cr <Plug>(coc-rename)

" Remap for format selected region
xmap <leader>cf  <Plug>(coc-format-selected)

augroup mygroup
  autocmd!
  " Setup formatexpr specified filetype(s).
  autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
  " Update signature help on jump placeholder
  autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
augroup end

" Remap for do codeAction of selected region, ex: `<leader>aap` for current paragraph
xmap <leader>ca  <Plug>(coc-codeaction-selected)
nmap <leader>ca  <Plug>(coc-codeaction-selected)

" Remap for do codeAction of current line
nmap <leader>ac  <Plug>(coc-codeaction)
" Fix autofix problem of current line
" nmap <leader>qf  <Plug>(coc-fix-current)

nmap <leader>cf :call CocAction('format')<CR>

" Add status line support, for integration with other plugin, checkout `:h coc-status`
set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}

" Using CocList
" Show all diagnostics
nnoremap <silent> <leader>cd  :<C-u>CocList diagnostics<cr>
" Manage extensions
nnoremap <silent> <leader>ce  :<C-u>CocList extensions<cr>
" Show commands
nnoremap <silent> <leader>cc  :<C-u>CocList commands<cr>
" Find symbol of current document
nnoremap <silent> <leader>co  :<C-u>CocList outline<cr>
" Search workspace symbols
nnoremap <silent> <leader>cs  :<C-u>CocList -I symbols<cr>
" Do default action for next item.
nnoremap <silent> <leader>cj  :<C-u>CocNext<CR>
" Do default action for previous item.
nnoremap <silent> <leader>ck  :<C-u>CocPrev<CR>
" Resume latest coc list
nnoremap <silent> <leader>cp  :<C-u>CocListResume<CR>
" }}}
" {{{ terraform config
let g:terraform_fold_sections=1
let g:terraform_align=1

let g:terraform_fmt_on_save=1
" }}}
" LanguageClient {{{

" let g:LanguageClient_serverCommands = {
    " \ 'python': ['pyls', '-vv', '--log-file', '~/logs/pyls.log'],
    " \ }
"
" let g:LanguageClient_settingsPath = "/home/kosciej/.vim/settings.json"
" nnoremap gd :call LanguageClient#textDocument_definition()<CR>

" nnoremap <leader>sr :call LanguageClient#textDocument_rename()<CR>
" nnoremap <leader>sf :call LanguageClient#textDocument_formatting()<CR>
" nnoremap <leader>st :call LanguageClient#textDocument_typeDefinition()<CR>
" nnoremap <leader>sx :call LanguageClient#textDocument_references()<CR>
" nnoremap <leader>sa :call LanguageClient_workspace_applyEdit()<CR>
" nnoremap <leader>sc :call LanguageClient#textDocument_completion()<CR>
" nnoremap <leader>sh :call LanguageClient#textDocument_hover()<CR>
" nnoremap <leader>ss :call LanguageClient_textDocument_documentSymbol()<CR>
" nnoremap <leader>sm :call LanguageClient_contextMenu()<CR>
" let g:LanguageClient_diagnosticsList = "Location"

" let g:LanguageClient_trace = "verbose"
" let g:LanguageClient_loggingFile = "/home/kosciej/logs"
" let g:LanguageClient_windowLogMessageLevel = "Log"
"

function! LoadConfig()
    let config = json_decode(system("cat /home/kosciej/.vim/settings.json"))
    call LanguageClient#Notify("workspace/didChangeConfiguration", { "settings": config })
endfunction
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


nmap <C-_> <Plug>NERDCommenterToggle
vmap <C-_> <Plug>NERDCommenterToggle
" }}}
" ultisnips config {{{
 " Trigger configuration. Do not use <tab> if you use https://github.com/Valloric/YouCompleteMe.
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<c-m>"
let g:UltiSnipsJumpBackwardTrigger="<c-b>"
let g:UltiSnipsListSnippets="lll"
nnoremap <leader>eu :UltiSnipsEdit<cr>
"let g:UltiSnipsSnippetDirectories=[".vim/bundle/vim-snippets/UltiSnips"]
let g:UltiSnipsSnippetsDir = "~/.vim/bundle/ultisnips/UltiSnips"

" If you want :UltiSnipsEdit to split your window.
let g:UltiSnipsEditSplit="vertical"
" }}}
" {{{ pytest config
let g:pytest_executable = "pytest"
nnoremap <leader>ta :Pytest project<cr>
nnoremap <leader>tf :Pytest file<cr>
nnoremap <leader>tm :Pytest function<cr>
nnoremap <leader>ts :Pytest session<cr>
nnoremap <leader>te :Pytest error<cr>
nnoremap <leader>tl :Pytest fails<cr>
nnoremap <leader>tc :Pytest clear<cr>
nnoremap <leader>t1 :Pytest first<cr>
nnoremap <leader>t0 :Pytest last<cr>
nnoremap <leader>t] :Pytest next<cr>
nnoremap <leader>t[ :Pytest previous<cr>
" }}}
" easymotion config {{{
let g:EasyMotion_do_mapping = 0 " Disable default mappings
nmap s <Plug>(easymotion-overwin-f2)

" Turn on case insensitive feature
let g:EasyMotion_smartcase = 1

" JK motions: Line motions
map <Leader>j <Plug>(easymotion-j)
map <Leader>k <Plug>(easymotion-k)
" }}}
" autoflake config {{{
let g:autoflake_remove_all_unused_imports=1
let g:autoflake_disable_show_diff=1
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
". }}}

" autocmd FileType python let b:coc_root_patterns = ['.git', '.env', 'cos', '.idea']

" let vimwiki_list = [{'path': '~/.config/nvim/vimwiki/'}]


let wiki_1 = {}
let wiki_1.path = '~/.config/nvim/vimwiki/personal'
let wiki_1.syntax = 'markdown'
let wiki_1.ext = '.md'

let wiki_2 = {}
let wiki_2.path = '~/.config/nvim/vimwiki/work'
let wiki_2.syntax = 'markdown'
let wiki_2.ext = '.md'

let g:vimwiki_list = [wiki_1, wiki_2]
let g:vimwiki_ext2syntax = {'.md': 'markdown', '.markdown': 'markdown', '.mdown': 'markdown'}
let vimwiki_map_prefix = "<leader>v"


function Moja()
    let g:v = expand('%:h:t')
    let g:n = expand('%:t:r')
    let s = g:v . '/' .  g:n
    put =s
    return g:v . '/' .  g:n
endfunction

nnoremap ab :call Moja()<CR>
