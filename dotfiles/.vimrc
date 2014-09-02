" syntax highlighting on
syn on

" indenting shits
set expandtab
set shiftwidth=4
set softtabstop=4
set tabstop=4
set nowrap
"set number
" auto indent after a {
set autoindent
set smartindent

au BufRead,BufNewFile *.scss set filetype=scss

autocmd FileType html setlocal expandtab shiftwidth=2 tabstop=2 softtabstop=2
autocmd FileType htmldjango setlocal expandtab shiftwidth=2 tabstop=2 softtabstop=2
autocmd FileType css setlocal expandtab shiftwidth=2 tabstop=2 softtabstop=2
autocmd FileType scss setlocal expandtab shiftwidth=2 tabstop=2 softtabstop=2
autocmd FileType javascript setlocal expandtab shiftwidth=2 tabstop=2 softtabstop=2
autocmd FileType php setlocal expandtab shiftwidth=2 tabstop=2 softtabstop=2
autocmd FileType xslt setlocal expandtab shiftwidth=2 tabstop=2 softtabstop=2
autocmd FileType xsd setlocal expandtab shiftwidth=2 tabstop=2 softtabstop=2
autocmd FileType python setlocal expandtab shiftwidth=4 tabstop=4 softtabstop=4

" encoding shits
" language nl_NL.utf8
" let &termencoding = &encoding
set fileencoding=utf-8
set encoding=utf-8

" case insensitive search
set ignorecase
set smartcase
set incsearch
set showmatch
set nohlsearch

" misc
set novisualbell " don't blink
set noerrorbells " no noises
set statusline=%F\ %m%r%h%w\ [line=%l/%L][%p%%]
set laststatus=2 " always show the status line

" Format Options
set formatoptions=ro

" Page nav
" noremap <Space> <PageDown>  " space voor pgdn
" noremap <BS> <PageUp>       " backspace voor pgup

" Scrolling
set scrolljump=5 " jump 5 regels bij scrollen
set scrolloff=3 " scroll bij 3 regels off the edge

" Folding
highlight Folded ctermbg=blue ctermfg=white
highlight FoldColumn ctermbg=darkgrey ctermfg=red

set errorformat=%m\ in\ %f\ on\ line\ %l
set commentstring=\ //\ %s
set wmh=0

" Colors
hi Comment ctermfg=blue 
hi TabLineSel ctermbg=2 ctermfg=7
hi TabLine ctermbg=7 ctermfg=0
hi Pmenu ctermbg=darkblue
hi PmenuSel ctermbg=cyan
hi PmenuSel ctermfg=white

autocmd vimenter * if !argc() | NERDTree | endif
