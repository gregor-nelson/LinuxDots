[[ -f ~/.Xresources ]] && xrdb -merge -I$HOME ~/.Xresources


xset r rate 150 75 &
picom &
redshift &
/etc/X11/xinit/xinitrc.d/80-bar-script.sh &

exec dwm
