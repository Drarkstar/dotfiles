#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

# neovim
export EDITOR='nvim'
export VISUAL='nvim'

# aliases
alias ll="ls -la"
alias la="ls -a"
alias shut="shutdown now"

# nitrogen (backgrounds)
# nitrogen --random --set-zoom-fill ~/backgrounds/

# starship
eval "$(starship init bash)"
