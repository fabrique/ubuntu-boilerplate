# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions
alias ls="ls --color=auto"
alias ll="ls -al --color=auto"
alias vi="vim"

PATH=$PATH:$HOME/.gem/ruby/1.8/bin/:$HOME/.gem/ruby/1.9.1/bin/:/var/lib/gems/1.8/bin/:/var/lib/gems/1.9.1/bin/
