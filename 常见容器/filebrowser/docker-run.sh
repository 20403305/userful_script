docker run -v C:/Users/EDY/Downloads/file_browser:/srv -v C:/Users/EDY/Downloads/file_browser/filebrowser.db:/database/filebrowser.db -v C:/Users/EDY/Downloads/file_browser/settings.json:/config/settings.json -p 8080:80 filebrowser/filebrowser:v2.31.2

docker run -d --name filebrowser -v C:/Users/EDY/Downloads/file_browser:/srv -v C:/Users/EDY/Downloads/file_browser/filebrowser.db:/database/filebrowser.db -v C:/Users/EDY/Downloads/file_browser/settings.json:/config/settings.json -p 8080:80  filebrowser/filebrowser:v2.31.2
