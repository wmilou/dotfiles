#!/bin/bash

echo "********************************************************"
echo "****************** Fixing Rofi Themes ******************"
echo "************ https://github.com/anilbeesetti ***********"
echo "********************************************************"
echo ""
echo ""


openbox_dir="$HOME/.config/rofi"
bspwm_dir="$HOME/.config/bspwm/rofi/themes"

themes=("default" "beach" "forest" "manhattan" "nordic" "spark" "wave" "beach-bitmap" "forest-bitmap")
apps=("launcher" "networkmenu" "powermenu" "mpd" "network" "screenshot")

append_to_file(){
    echo "
element-text, element-icon {
    background-color: inherit;
    text-color:       inherit;
}
" >> $1
}

# Fixing Openbox themes
echo "Fixing Openbox and Bspwm themes"
echo "------------------------------------------------"
for theme in ${themes[@]}
do
    echo "## patching ${theme} theme"
    for app in ${apps[@]}
    do
        grep -q 'element-text, element-icon {
    background-color: inherit;
    text-color:       inherit;' $openbox_dir/$theme/$app.rasi
        if [[ $? == 0 ]]
        then
                continue
        fi
        append_to_file $openbox_dir/$theme/$app.rasi
    done
    
done


## Fixing Bspwm themes
echo "## patching bspwm themes"
for file in $(ls $bspwm_dir)
do
    if [[ $file == 'askpass.rasi'  ||  $file == "confirm.rasi"  ||  $file == "colors.rasi" ]]
    then
        continue
    fi
    grep -q 'element-text, element-icon {
    background-color: inherit;
    text-color:       inherit;' $bspwm_dir/$file
    if [[ $? == 0 ]]
    then
            continue
    fi
    append_to_file $bspwm_dir/$file
done


echo ""
echo ""
echo "Done patching. You may have to logout and relogin to fix the rofi themes.."
echo "---------------------------------------------------"
