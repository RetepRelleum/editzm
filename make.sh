source .venv/bin/activate
# pyside6-rcc -o resources.py resources.qrc
# deactivate

rm -r -f /home/retep/.local/share/QGIS/QGIS4/profiles/default/python/plugins/editzm
mkdir /home/retep/.local/share/QGIS/QGIS4/profiles/default/python/plugins/editzm

cp  /home/retep/editzm/icon.png         /home/retep/.local/share/QGIS/QGIS4/profiles/default/python/plugins/editzm/icon.png 
cp  /home/retep/editzm/metadata.txt     /home/retep/.local/share/QGIS/QGIS4/profiles/default/python/plugins/editzm/metadata.txt
cp  /home/retep/editzm/__init__.py      /home/retep/.local/share/QGIS/QGIS4/profiles/default/python/plugins/editzm/__init__.py
cp  /home/retep/editzm/EditZM.py        /home/retep/.local/share/QGIS/QGIS4/profiles/default/python/plugins/editzm/EditZM.py
cp  /home/retep/editzm/EditZM_dialog.py /home/retep/.local/share/QGIS/QGIS4/profiles/default/python/plugins/editzm/EditZM_dialog.py
cp  /home/retep/editzm/GeomMupe.py      /home/retep/.local/share/QGIS/QGIS4/profiles/default/python/plugins/editzm/GeomMupe.py
cp /home/retep/editzm/EditZM_Series.py  /home/retep/.local/share/QGIS/QGIS4/profiles/default/python/plugins/editzm/EditZM_Series.py
cp  /home/retep/editzm/LICENSE          /home/retep/.local/share/QGIS/QGIS4/profiles/default/python/plugins/editzm/LICENSE

