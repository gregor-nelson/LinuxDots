export EDITOR=nvim
setopt PROMPT_SUBST
VIM_MODE=""
PS1=$'${VIM_MODE}%B%F{33}[%b%F{255}%n%B%F{33}@%b%F{245}%M %b%F{255}%~%B%F{33}] %F{75}\uf303%f%b '

HISTSIZE=1000000
SAVEHIST=1000000
HISTFILE=~/.zsh_history

setopt SHARE_HISTORY
setopt EXTENDED_HISTORY
setopt HIST_REDUCE_BLANKS

autoload -Uz compinit
zstyle ':completion:*' menu select
zmodload zsh/complist

if [[ -n ~/.zcompdump(#qN.mh+24) ]]; then
    compinit
else
    compinit -C
fi

_comp_options+=(globdots)

zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'

setopt COMPLETE_IN_WORD
setopt ALWAYS_TO_END
setopt MENU_COMPLETE
setopt LIST_PACKED
setopt LIST_TYPES
setopt REC_EXACT

bindkey -v
export KEYTIMEOUT=1

bindkey -M menuselect 'h' vi-backward-char
bindkey -M menuselect 'k' vi-up-line-or-history
bindkey -M menuselect 'l' vi-forward-char
bindkey -M menuselect 'j' vi-down-line-or-history
bindkey -v '^?' backward-delete-char

function zle-keymap-select {
  if [[ ${KEYMAP} == vicmd ]] ||
     [[ $1 = 'block' ]]; then
    echo -ne '\e[1 q'
    VIM_MODE=$'%B%F{green}\ue62b%f%b '
  elif [[ ${KEYMAP} == main ]] ||
       [[ ${KEYMAP} == viins ]] ||
       [[ ${KEYMAP} = '' ]] ||
       [[ $1 = 'beam' ]]; then
    echo -ne '\e[5 q'
    VIM_MODE=""
  fi
  zle reset-prompt
}
zle -N zle-keymap-select

zle-line-init() {
    zle -K viins
    echo -ne "\e[5 q"
    VIM_MODE=""
}
zle -N zle-line-init

echo -ne '\e[5 q'
autoload -Uz add-zsh-hook
_reset_cursor() { echo -ne '\e[5 q'; }
add-zsh-hook preexec _reset_cursor

autoload edit-command-line; zle -N edit-command-line
bindkey '^e' edit-command-line

setopt AUTO_CD
setopt AUTO_PUSHD
setopt PUSHD_IGNORE_DUPS
setopt PUSHD_SILENT
setopt PUSHD_TO_HOME
setopt CDABLE_VARS

setopt EXTENDED_GLOB
setopt GLOB_DOTS
setopt NUMERIC_GLOB_SORT
setopt NULL_GLOB

setopt NO_CLOBBER
setopt INTERACTIVE_COMMENTS
setopt CORRECT
setopt AUTO_PARAM_SLASH
setopt AUTO_REMOVE_SLASH
setopt AUTO_LIST
setopt MAGIC_EQUAL_SUBST
setopt LONG_LIST_JOBS
setopt PRINT_EIGHT_BIT
setopt IGNORE_EOF

export LS_COLORS="${LS_COLORS}:ow=01;34:tw=01;34"

alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'

alias ls='ls --color=auto'
alias ll='ls -lah'
alias la='ls -A'
alias l='ls -CF'

alias grep='grep --color=auto'
alias fgrep='grep -F --color=auto'
alias egrep='grep -E --color=auto'

alias reload='source ~/.zshrc'
alias zshconfig='$EDITOR ~/.zshrc'
alias chromium='chromium --disable-features=ExtensionManifestV2Unsupported,ExtensionManifestV2Disabled'

alias mot_server='ssh -C debian@57.128.170.234'
alias dev_server='ssh -C debian@51.178.139.7'



[[ ":$PATH:" != *":$HOME/.local/bin:"* ]] && export PATH="$HOME/.local/bin:$PATH"

ZSH_PLUGIN_DIR="${HOME}/.local/share/zsh/plugins"


[[ -f "${ZSH_PLUGIN_DIR}/zsh-autosuggestions/zsh-autosuggestions.zsh" ]] && \
    source "${ZSH_PLUGIN_DIR}/zsh-autosuggestions/zsh-autosuggestions.zsh"


[[ -f "${ZSH_PLUGIN_DIR}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" ]] && \
    source "${ZSH_PLUGIN_DIR}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"
