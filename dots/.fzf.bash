# Setup fzf
# ---------
if [[ ! "$PATH" == */home/kosciej/.fzf/bin* ]]; then
  export PATH="${PATH:+${PATH}:}/home/kosciej/.fzf/bin"
fi

# Auto-completion
# ---------------
[[ $- == *i* ]] && source "/home/kosciej/.fzf/shell/completion.bash" 2> /dev/null

# Key bindings
# ------------
source "/home/kosciej/.fzf/shell/key-bindings.bash"
