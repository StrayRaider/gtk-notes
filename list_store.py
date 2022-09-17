
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="window title")
        self.main_box = Gtk.VBox()
        self.add(self.main_box)
        #treeview ve list store oluşturulması
        #list store oluştururken sütunların hangi tipte değişken tutacağı belirtilir
        self.song_store = Gtk.ListStore(str,bool)
        self.songtree = Gtk.TreeView(self.song_store)
        #içinde tutacağı değişken tipine göre bölme oluşturulması
        cell = Gtk.CellRendererText()
        #cell.set_property("editable", True) #eğer tect değiştirilebilir olsun istersen
        #stun tanımlama işlemi 1. argüman stun adı, 2. tutacağı hücre tipi 3, ekleme
        #yaparken listenin kaçıncı argümanını alacağı
        column = Gtk.TreeViewColumn("deneme",cell,text = 0)

        #check button stunu oluşturma işlemi
        #uygun hücre oluşturma
        check_cell = Gtk.CellRendererToggle()
        #hücre içi widget fonksiyon bağlantısı
        check_cell.connect("toggled", self.tree_but_toggle,1)
        #satır oluşturma 1. satır adı 2. hücre tipi
        t_column = Gtk.TreeViewColumn("deneme",check_cell)
        #stuna argümanları dışarda bu fonksiyonla da verebilirsin
        t_column.add_attribute(check_cell,"active",1)

        #stun treeview ekleme işlemi
        self.songtree.append_column(t_column)
        self.songtree.append_column(column)
 
        #yeni satırlar oluşturma
        self.song_store.append(["deneme",True])
        self.song_store.append(["deneme",False])
        self.main_box.pack_start(self.songtree,0,0,10)


    def tree_but_toggle(self, widget, path, column):
        print(path,column)
        self.song_store[path][column] = not self.song_store[path][column]
        print("toggled")




win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
