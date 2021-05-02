
#!/usr/bin/env bash

# -----------------------------------------------------------------------------
# Info:
#   author:    Miroslav Vidovic
#   file:      web-search.sh
#   created:   24.02.2017.-08:59:54
#   revision:  ---
#   version:   1.0
# -----------------------------------------------------------------------------
# Requirements:
#   rofi
# Description:
#   Use rofi to search the web.
# Usage:
#   web-search.sh
# -----------------------------------------------------------------------------
# Script:
#Theme for rofi

declare -A URLS

URLS=(
  ["google"]="https://www.google.com/search?q="
  ["bing"]="https://www.bing.com/search?q="
  ["yahoo"]="https://search.yahoo.com/search?p="
  ["duckduckgo"]="https://www.duckduckgo.com/?q="
  ["github"]="https://github.com/search?q="
  ["stackoverflow"]="http://stackoverflow.com/search?q="
  ["searchcode"]="https://searchcode.com/?q="
  ["openhub"]="https://www.openhub.net/p?ref=homepage&query="
  ["superuser"]="http://superuser.com/search?q="
  ["askubuntu"]="http://askubuntu.com/search?q="
  ["imdb"]="http://www.imdb.com/find?ref_=nv_sr_fn&q="
  ["piratebay"]="https://thepiratebay.org/search/"
  ["youtube"]="https://www.youtube.com/results?search_query="
  ["vimawesome"]="http://vimawesome.com/?q="
)

# List for rofi
gen_list() {
    for i in "${!URLS[@]}"
    do
      echo "$i"
    done
}

main() {
  # Pass the list to rofi
  platform=$( (gen_list) | rofi -config ~/.config/rofi/custom_scripts/themes/config.simple -dmenu -padding 18 -width 40 -location 0 -lines 5 -columns 3 -show-icons -icon-theme 'Papirus' -font 'Fantasque Sans Mono 20' -p "Searcher") 

  if [[ -n "$platform" ]]; then
    query=$( (echo ) |  rofi -config ~/.config/rofi/custom_scripts/themes/config.simple -dmenu -padding 20 -lines 0 -width 40 -location 0 -font 'Fantasque Sans Mono 20' -p "Query")
       # rofi -dmenu -matching fuzzy -location 0 -p "Query > " )

    if [[ -n "$query" ]]; then
      url=${URLS[$platform]}$query
      xdg-open "$url"
    else
      exit
    fi

  else
    exit
  fi
}

main

exit 0
