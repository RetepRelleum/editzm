# coding=utf-8
"""Lifecycle tests: classFactory -> initGui -> unload."""

from unittest.mock import MagicMock


def test_class_factory_returns_instance(qgis_iface):
    """classFactory returns a plugin instance."""
    from EditZM.EditZM import EditZM
    plugin = EditZM(qgis_iface)
    assert plugin is not None


def test_init_gui_registers_action(qgis_iface):
    """initGui registers an action for the plugin."""
    from EditZM.EditZM import EditZM
    plugin = EditZM(qgis_iface)
    plugin.initGui()
    assert plugin.actions
    plugin.unload()


def test_unload_removes_action(qgis_iface, monkeypatch):
    """unload removes the toolbar icon via iface."""
    from EditZM.EditZM import EditZM
    remove_toolbar_icon = MagicMock()
    monkeypatch.setattr(qgis_iface, "removeToolBarIcon", remove_toolbar_icon)
    plugin = EditZM(qgis_iface)
    plugin.initGui()
    plugin.unload()
    remove_toolbar_icon.assert_called()
