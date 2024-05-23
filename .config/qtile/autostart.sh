#!/bin/sh
#dunst -conf /home/jorge/.config/dunst/qtilerc &
nm-applet &
cbatticon -n -i standard BAT1 &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
alacritty &
firefox &