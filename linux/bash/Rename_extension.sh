#Method-1
rename .html .txt *.html 

#usage:
#rename [find] [replace_with] [criteria]

#Method-2
for file in *.html
do
  mv "$file" "${file%.html}.txt"
done

#Method-3
for file in *.html; do
    mv "$file" "$(basename "$file" .html).txt"
done

#Method-4
find . -name "*.js" -exec bash -c 'mv "$1" "${1%.js}".tsx' - '{}' \;

