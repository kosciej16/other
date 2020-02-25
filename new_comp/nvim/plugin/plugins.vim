if empty(glob('~/.local/share/nvim/site/autoload/plug.vim'))
  silent !curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/bundle')

" Plug 'airblade/vim-gitgutter'
Plug 'alfredodeza/pytest.vim'
Plug 'altercation/vim-colors-solarized'
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
Plug 'neoclide/coc.nvim', {'branch': 'release'}
" Plug 'rafi/awesome-vim-colorschemes'
" Plug 'rizzatti/dash.vim'
Plug 'rking/ag.vim'
Plug 'scrooloose/nerdcommenter'
Plug 'scrooloose/nerdtree'
" Plug 'sheerun/vim-polyglot'
" Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'SirVer/ultisnips'
" Plug 'sodapopcan/vim-twiggy'
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
Plug 'tpope/vim-rsi'
" Plug 'tpope/vim-sensible'
Plug 'tpope/vim-surround'
Plug 'tpope/vim-unimpaired'
Plug 'tpope/vim-rhubarb'

Plug 'vim-airline/vim-airline'
Plug 'FooSoft/vim-argwrap'
" Plug 'vim-airline/vim-airline-themes'
" Plug 'wellle/targets.vim'

" Plug 'inside/vim-search-pulse'
"
Plug 'mgedmin/python-imports.vim'
Plug 'lambdalisue/suda.vim'
Plug 'tell-k/vim-autoflake'
Plug 'yuttie/comfortable-motion.vim'


call plug#end()
filetype plugin indent on    " required
