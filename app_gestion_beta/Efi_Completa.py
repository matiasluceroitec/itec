from wx import *
from wx.dataview import *
import sqlite3
from wx.adv import *
import webbrowser
import os

class MyApp(App):
    def OnInit(self):
        #listacaja = self.listacaja = []
        self.listaCli = []
        self.listaArt = []
        self.BuscarArt = []
        self.listaPrecio = []
        self.listaProveedores = []
        NOMBRE =self.NOMBRE=""
        f = self.Frame = Frame(None, -1, self.NOMBRE, pos=(0, 0), size=(1000, 750),style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER )
        p = self.p = Panel(f)
        BoxH = BoxSizer(HORIZONTAL)
        GB = GridBagSizer(1, 6)
        BoxH.Add(GB)

        ico=self.ico = Icon('loguito.ico', BITMAP_TYPE_ICO)
        f.SetIcon(ico)

        self.FND=FND="Fondo3.jpg"
        fondo = Image('Fondo3.jpg', BITMAP_TYPE_ANY)
        Fondo = StaticBitmap(p, -1, Bitmap(fondo))

        mapaDEbits = Image('Logo.jpg', BITMAP_TYPE_ANY)  # el ANY es pa cualquier formato
        imagen = StaticBitmap(p, -1, Bitmap(mapaDEbits))  # no tenia tornillos para poner

        art = Bitmap('articulos.bmp', BITMAP_TYPE_BMP)
        BotArticulos = self.BotArticulos = BitmapButton(p, -1, art)
        avatar = Bitmap('clientes.bmp', BITMAP_TYPE_BMP)
        BotClientes = self.BotClientes = BitmapButton(p, -1, avatar)
        cash = Bitmap('caja.bmp', BITMAP_TYPE_BMP)
        BotCaja = self.BotCaja = BitmapButton(p, -1,cash)
        opc=Bitmap('opciones.bmp', BITMAP_TYPE_BMP)
        BotOpciones = self.BotOpciones = BitmapButton(p, -1, opc)
        pro=Bitmap('proveedor.bmp', BITMAP_TYPE_BMP)
        BotProveedores = self.BotProveedores = BitmapButton(p, -1,pro)
        calcu=Bitmap('calculadora.bmp', BITMAP_TYPE_BMP)
        BotCalculadora=BitmapButton(p,-1,calcu)
        BotCalculadora.Bind(EVT_BUTTON,self.calculadora)


        #Fecha y Hora
        DAY= str(DateTime.Today())
        DAY= DAY[:-8]
        Dia=self.Dia= StaticText(p,-1,DAY)

        #Funciones de los botones
                        #FRAMES
        carro = Bitmap('venta.bmp', BITMAP_TYPE_BMP)
        BotVentas = self.BotVentas = BitmapButton(p, -1, carro)
        self.BotVentas.Bind(EVT_BUTTON,self.Ventas)
        self.BotOpciones.Bind(EVT_BUTTON,self.Opciones)
        self.BotArticulos.Bind(EVT_BUTTON, self.articulos)
        self.BotClientes.Bind(EVT_BUTTON, self.clientes)
        self.BotCaja.Bind(EVT_BUTTON, self.caja)
        self.BotProveedores.Bind(EVT_BUTTON, self.Proveedores)
        #POSICIONES
        GB.Add(BotVentas, pos=(1, 0))
        GB.Add(BotArticulos, pos=(2, 0))
        GB.Add(BotClientes, pos=(3, 0))
        GB.Add(BotCaja, pos=(4, 0))
        GB.Add(BotOpciones, pos=(5, 0))
        GB.Add(BotProveedores, pos=(6, 0))
        GB.Add(imagen, pos=(0, 0))
        GB.Add(BotCalculadora,pos=(7,0))
        #BoxH.Add(Dia)
        BoxH.Add(Fondo)
        p.SetSizer(BoxH)


        f.Show()
        return True

#FRAME DE CAJA
    def caja (self, evt):

        fCaja = self.fCaja = Frame(None, -1, "CAJA DIARIA", size=(700, 600))
        fCaja.SetBackgroundColour(WHITE)
        pCaja = self.pCaja = Panel(fCaja)  # LE METO EL PANEL
        Box = BoxSizer(VERTICAL)
        # Grillas
        grilla1 = GridBagSizer(10, 10)
        grilla2 = GridBagSizer(10, 10)
        Box.Add(grilla1)
        Box.Add(grilla2)
        # Botones
        jpeg = Bitmap('cancelar.bmp', BITMAP_TYPE_BMP)
        BotCierra = self.bmpbtn = BitmapButton(pCaja, -1, jpeg)
        jpeg = Bitmap('aceptar.bmp', BITMAP_TYPE_BMP)
        BotProcesa = self.bmpbtn1 = BitmapButton(pCaja, -1, jpeg)
        BotProcesa.Bind(EVT_BUTTON, self.procesacaja)
        BotCorte = self.BotCorte = Button(pCaja, -1, "Ver Cajas", size=(180, 50))
        self.BotCorte.Bind(EVT_BUTTON, self.cajafinal)
        BotCorte.SetBackgroundColour(WHITE)
        # TEXTOS ESTATITOS Y CAJAS DE TEXTOS
        hoy = self.hoy = str(DateTime.Today())
        hoy = self.hoy = hoy[3:5] + "/" + hoy[:2] + "/19" + hoy[6:8]
        l_fecha = StaticText(pCaja, -1, "Fecha:")
        fecha = self.fecha = TextCtrl(pCaja, -1, hoy)
        self.fecha.Bind(EVT_LEFT_DOWN, self.abrirCal)
        textCaja = StaticText(pCaja, -1, "Caja:")
        # l_separ = StaticText(pCaja, -1, "----------------------------------------")
        l_cantIn = StaticText(pCaja, -1, "Cantidad Inicial")
        l_cantIn.Bind(EVT_CHAR,self.error)
        cantIn = self.cantIn = TextCtrl(pCaja, -1, "0", (100, 50), (200, 25))
        l_Efec = StaticText(pCaja, -1, "Efectivo")
        efec = self.efec = StaticText(pCaja, -1, "", (100, 50), (200, 25))
        l_cred = StaticText(pCaja, -1, "Tarjetas de credito")
        cred = self.cred = StaticText(pCaja, -1, "", (100, 50), (200, 25))
        l_deb = StaticText(pCaja, -1, "Cuenta corriente")
        deb = self.deb = StaticText(pCaja, -1, "", (100, 50), (200, 25))
        l_total = StaticText(pCaja, -1, "TOTAL")
        total = self.total = StaticText(pCaja, -1, "", (100, 50), (200, 25))
        self.cajas = ["Mario", "Isco", "Santi", "Matias", "Giuli", "Todas"]
        self.Cajas = ComboBox(pCaja, -1, "Cajero:", (90, 50), (160, -1), self.cajas, CB_DROPDOWN | TE_PROCESS_ENTER)
        # Ubicaciones
        grilla1.Add(l_fecha, pos=(1, 0))
        grilla1.Add(fecha, pos=(2, 0))
        grilla1.Add(self.Cajas, pos=(4, 0))
        grilla1.Add(textCaja, pos=(3, 0))
        grilla1.Add(l_cantIn, pos=(5, 0))
        grilla1.Add(cantIn, pos=(6, 0))
        grilla1.Add(l_Efec, pos=(7, 0))
        grilla1.Add(efec, pos=(8, 0))
        grilla1.Add(l_cred, pos=(9, 0))
        grilla1.Add(cred, pos=(10, 0))
        grilla1.Add(l_deb, pos=(11, 0))
        grilla1.Add(deb, pos=(12, 0))
        grilla2.Add(BotCierra, pos=(1, 2))
        grilla2.Add(BotProcesa, pos=(1, 4))
        grilla1.Add(BotCorte, pos=(11, 6))
        grilla1.Add(l_total, pos=(8, 6))
        grilla1.Add(total, pos=(9, 6))

        pCaja.SetSizer(Box)
        fCaja.Show()
        return True

#FRAME DE VENTAS
    def Ventas(self, evt):
        f2 = self.f2 = Frame(None, -1, "Ventas", pos=(143, 26), size=(900, 700))
        p2 = self.p2 = Panel(f2)
        f2.SetIcon(self.ico)
        # FND2='Fondo3.jpg'
        # fondo =self.fondo= Image(FND2, BITMAP_TYPE_ANY)
        # Fondo = self.Fondo =StaticBitmap(p2, -1, Bitmap(fondo))
        BoxZ = BoxSizer(VERTICAL)
        GBZ = GridBagSizer(10, 10)
        GBZ0 = GridBagSizer(10, 10)

        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        cur.execute("SELECT * FROM Clientes")
        ROWS = cur.fetchall()
        for ROW in ROWS:
            self.listaCli.append(ROW[2])
        con.close()

        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        cur.execute("SELECT * FROM Articulos")
        ROWS = cur.fetchall()
        for ROW in ROWS:
            self.listaArt.append(ROW[2])
        con.close()

        # LISTA CONTROL
        self.dvlc = dvlc = DataViewListCtrl(p2, size=(605, 300))
        encabezado = [('Codigo', 130), ('Producto', 250), ('Cantidad', 75), ('Stock', 75), ('Precio', 75)]
        for enca in encabezado:
            dvlc.AppendTextColumn(enca[0], width=enca[1])

        self.ch = Choice(p2, -1, (100, 50), choices=self.listaCli, size=(400, 25))
        self.ch1 = Choice(p2, -1, (100, 50), choices=self.listaArt, size=(400, 25))

        self.cajeros = ["Mario", "Isco", "Santi", "Matias", "Giuli"]
        self.Cajeros = ComboBox(p2, -1, "Cajero:", (90, 50), (160, -1), self.cajeros, CB_DROPDOWN | TE_PROCESS_ENTER)

        # BOTONES_TEXCRTL_STATICTEXT
        ticket = self.ticket = StaticText(p2, -1, "Cantidad")
        FECHA = str(DateTime.Today())
        FECHA = "FECHA  " + FECHA[:-8]
        fecha = self.fecha = StaticText(p2, -1, FECHA)
        TextoCliente = StaticText(p2, -1, "CLIENTE :")
        BotonBuscar = Button(p2, -1, "BUSCAR", size=(100, 25))
        CajaCantidad = self.CajaCantidad = TextCtrl(p2, -1, "1", size=(50, 25))
        CajaCantidad.Bind(EVT_CHAR,self.error)
        BotonListado = self.BotonListado = Button(p2, -1, "LISTADO", size=(100, 25))
        CajaDesc = self.BotonDesc = TextCtrl(p2, -1, "0", size=(100, 25))
        CajaDesc.Bind(EVT_CHAR,self.error)
        TextoDescuento=StaticText(p2,-1,"Descuento :")
        CajaPaga = self.CajaPaga = TextCtrl(p2, -1, "0", size=(100, 25))
        TextoPaga=StaticText(p2,-1,"Paga :")
        CajaPaga.Bind(EVT_CHAR,self.error)
        TextVuelto = self.TextVuelto = StaticText(p2, -1, "Su Vuelto")
        CajaVuelto = self.CajaVuelto = StaticText(p2, -1)
        self.CajaVuelto.SetLabel("0")
        TextTotal = self.TextTotal = StaticText(p2, -1, "TOTAL :")
        TextSuma = self.TextSuma = StaticText(p2, -1)
        self.TextSuma.SetLabel("0")
        BotonCargar = self.BotonCarga = Button(p2, -1, "CARGAR", size=(100, 50))

        # RADIO BOX
        radio = ["EFECTIVO", "TARJETA", "CUENTA CORRIENTE"]
        self.rb = RadioBox(p2, -1, "Forma de pago", DefaultPosition, DefaultSize, radio, 1)

        # BOTONES ACEPTAR Y CANCELAR
        bmp = Bitmap('cancelar.bmp', BITMAP_TYPE_BMP)
        self.bmpbtn = BitmapButton(p2, -1, bmp)
        self.bmpbtn.Bind(EVT_BUTTON, self.Cancelar)

        bmp1 = Bitmap('aceptar.bmp', BITMAP_TYPE_BMP)
        self.bmpbtn1 = BitmapButton(p2, -1, bmp1)
        self.bmpbtn1.Bind(EVT_BUTTON, self.Cobrar)

        # CARGAR
        self.BotonCarga.Bind(EVT_BUTTON, self.CargarDatosART)

        # Posiciones
        BoxZ.Add(GBZ)
        BoxZ.Add(GBZ0)
        GBZ.Add(ticket, (1, 1))
        GBZ.Add(fecha, (2, 1))
        GBZ.Add(TextoCliente, (1, 2))
        GBZ.Add(self.ch, (1, 3))
        GBZ.Add(BotonBuscar, (1, 4))
        GBZ.Add(CajaCantidad, (2, 2))
        GBZ.Add(self.ch1, (2, 3))
        GBZ.Add(BotonListado, (2, 4))
        GBZ0.Add(dvlc, (2, 2), span=(5, 7))
        GBZ0.Add(TextoDescuento,pos=(3,0))
        GBZ0.Add(CajaDesc, pos=(4, 0))
        GBZ0.Add(TextoPaga,pos=(9,1))
        GBZ0.Add(CajaPaga, pos=(9, 2))
        GBZ0.Add(TextVuelto, pos=(9, 3))
        GBZ0.Add(CajaVuelto, pos=(9, 4))
        GBZ0.Add(TextTotal, pos=(8, 2))
        GBZ0.Add(TextSuma, pos=(8, 3))
        GBZ0.Add(self.bmpbtn1, pos=(8, 7))
        GBZ0.Add(self.bmpbtn, pos=(8, 6))
        GBZ0.Add(self.rb, pos=(2, 0))
        GBZ0.Add(BotonCargar, pos=(5, 0))
        GBZ.Add(self.Cajeros, pos=(0, 0))

        p2.SetSizer(BoxZ)

        f2.Show()
        return True

#FRAME DE OPCIONES
    def Opciones(self,evt):
        f3 = self.f3 = Frame(None, -1, "Opciones", pos=(143, 26), size=(700, 300))
        p3 = self.p3 = Panel(f3)
        GBZOp=GridBagSizer(10,10)
        f3.SetIcon(self.ico)
        #Botones-Cajas Y Textos

        TextoNombre = StaticText(p3, -1,"Evaluacion Final Integradora")
        TextoPara=StaticText(p3, -1,"Materia:")
        TextoPara1=StaticText(p3, -1,"Programacion I")
        TextoCrea=StaticText(p3, -1,"Desarrollado por:")
        TextoInt=StaticText(p3, -1,"GARRIONE, Francisco - LUCERO, Matias")
        TextoFec=StaticText(p3, -1,"Noviembre 2018")

        in1 = Bitmap('in.bmp', BITMAP_TYPE_BMP)
        BotonIN = self.BotonIN = BitmapButton(p3, -1, in1)
        BotonIN.Bind(EVT_BUTTON,self.abrirurl)

        GBZOp.Add(TextoNombre, pos=(1, 1))
        GBZOp.Add(TextoPara, pos=(2,1))
        GBZOp.Add(TextoPara1, pos=(3,1))
        GBZOp.Add(TextoCrea, pos=(4,1))
        GBZOp.Add(TextoInt, pos=(5,1))
        GBZOp.Add(TextoFec, pos=(0,1))
        GBZOp.Add(BotonIN,pos=(6,1))



        p3.SetSizerAndFit(GBZOp)
        f3.Show()
        return True

#FRAME DE ARTICULOS
    def articulos(self, evt):
        fArticulo = self.Frame = Frame(None, -1, "ARTICULOS", pos=(0, 0), size=(1000, 900))
        pArticulo = self.pArticulo = Panel(fArticulo)
        #fArticulo.SetBackgroundColour(colour=(0, 255, 255))
        dvlc = self.dvlc = DataViewListCtrl(pArticulo, size=(650, 400))
        encabezado = [('CODIGO', 100), ('DESCRIPCION', 150), ('MARCA', 100), ('COSTO', 100),
                          ('PRECIO', 100), ('STOCK', 100)]
        for enca in encabezado:
            dvlc.AppendTextColumn(enca[0], width=enca[1])
        Box = BoxSizer(VERTICAL)
# GRILLAS
        grilla1 = GridBagSizer(10, 10)
        grilla2 = GridBagSizer(10, 10)
        grilla3 = GridBagSizer(10, 10)
        Box.Add(grilla1)
        Box.Add(grilla2)
        Box.Add(grilla3)

        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        cur.execute("SELECT * FROM Articulos")
        ROWS = cur.fetchall()
        for ROW in ROWS:
            self.listaArt.append(ROW[2])
        con.close()

        self.op = Choice(pArticulo, -1, (100, 50), choices=self.listaArt, size=(400, 25))

# BOTONES
        BotBusqueda = self.BotBusqueda = Button(pArticulo, -1, "BUSQUEDA", size=(100, 50))
        BotBusqueda.SetBackgroundColour(WHITE)
        BotBusqueda.Bind(EVT_BUTTON, self.BusquedaArt)
        BotTodos = self.BotTodos = Button(pArticulo, -1, "TODOS", size=(100, 50))
        BotTodos.SetBackgroundColour(WHITE)
        BotTodos.Bind(EVT_BUTTON, self.cargarBDART)
        BotStock = self.BotStock = Button(pArticulo, -1, "EN STOCK", size=(100, 50))
        BotStock.SetBackgroundColour(WHITE)
        BotStock.Bind(EVT_BUTTON, self.cargarBDARTStock)
        BotSinStock = self.BotBusqueda = Button(pArticulo, -1, "SIN STOCK", size=(100, 50))
        BotSinStock.SetBackgroundColour(WHITE)
        BotSinStock.Bind(EVT_BUTTON, self.cargarBDARTSinStock)
        BotStockMenosA = self.BotTodos = Button(pArticulo, -1, "STOCK MENOS A", size=(100, 50))
        BotStockMenosA.SetBackgroundColour(WHITE)
        BotStockMenosA.Bind(EVT_BUTTON, self.cargarBDARTStockMenosA)
        BotNuevo = self.BotStock = Button(pArticulo, -1, "NUEVO", size=(100, 50))
        BotNuevo.SetBackgroundColour(WHITE)
        BotNuevo.Bind(EVT_BUTTON, self.ArticuloNuevo)
        BotEditar = self.BotBusqueda = Button(pArticulo, -1, "EDITAR", size=(100, 50))
        BotEditar.SetBackgroundColour(WHITE)
        BotEditar.Bind(EVT_BUTTON, self.EditarArt)
        BotBorrar = self.BotTodos = Button(pArticulo, -1, "BORRAR", size=(100, 50))
        BotBorrar.SetBackgroundColour(WHITE)
        BotBorrar.Bind(EVT_BUTTON, self.BorrarArt)
        #BotCancelar = self.BotBusqueda = Button(pArticulo, -1, "CANCELAR", size=(100, 50))
        #BotCancelar.SetBackgroundColour(WHITE)
        #BotAceptar = self.BotTodos = Button(pArticulo, -1, "ACEPTAR", size=(100, 50))
        #BotAceptar.SetBackgroundColour(WHITE)

# Stock menos a - Caja de Texto
        numero = self.numero = TextCtrl(pArticulo, -1, "0", (100, 50), (50, 49))
        numero.Bind(EVT_CHAR,self.error)

# Ubicaciones
        grilla1.Add(BotBusqueda, pos=(1, 0))
        grilla1.Add(self.op, pos=(1, 1))
        grilla2.Add(self.dvlc, pos=(1, 0), span=(4, 5))  # depende los cuadros es la cantidad del numero
        grilla2.Add(BotTodos, pos=(1, 7))
        grilla2.Add(BotStock, pos=(2, 7))
        grilla2.Add(BotSinStock, pos=(3, 7))
        grilla2.Add(BotStockMenosA, pos=(4, 7))
        grilla2.Add(self.numero, pos=(4, 8))
        grilla3.Add(BotNuevo, pos=(1, 0))
        grilla3.Add(BotEditar, pos=(1, 1))
        grilla3.Add(BotBorrar, pos=(1, 2))
        #grilla3.Add(BotCancelar, pos=(1, 16))
        #grilla3.Add(BotAceptar, pos=(1, 17))

        pArticulo.SetSizer(Box)
        fArticulo.Show()

    def ArticuloNuevo(self, evt):
        fListado = self.fListado = Frame(None, -1, "Sistema administrativo - CREAR ARTICULO", size=(1500, 900))
        fListado.SetBackgroundColour(WHITE)
        pListado = Panel(fListado)  # LE METO EL PANEL
        BOX = BoxSizer(VERTICAL)
# Grillas
        grilla1 = GridBagSizer(10, 10)
        grilla2 = GridBagSizer(10, 30)
        grilla3 = GridBagSizer(10, 10)
        grilla4 = GridBagSizer(10, 10)
        BOX.Add(grilla1)
        BOX.Add(grilla2)
        BOX.Add(grilla3)
        BOX.Add(grilla4)
# Botones
        #BotNuevo = self.BotNuevo = Button(pListado, -1, "NUEVO", size=(100, 50))
        #BotNuevo.SetBackgroundColour(WHITE)
        #BotEditar = self.BotEditar = Button(pListado, -1, "EDITAR", size=(100, 50))
        #BotEditar.SetBackgroundColour(WHITE)
        #BotBorrar = self.BotBorrar = Button(pListado, -1, "BORRAR", size=(100, 50))
        #BotBorrar.SetBackgroundColour(WHITE)
        jpeg = Bitmap('cancelar.bmp', BITMAP_TYPE_BMP)
        BotCancelar = self.bmpbtn = BitmapButton(pListado, -1, jpeg)
        jpeg = Bitmap('aceptar.bmp', BITMAP_TYPE_BMP)
        BotAceptar = self.bmpbtn1 = BitmapButton(pListado, -1, jpeg)
        BotAceptar.Bind(EVT_BUTTON, self.CargarDatos)
# TEXTOS ESTATITOS Y CAJAS DE TEXTOS
        #l_busq = StaticText(pListado, -1, "BUSQUEDA")
        #busq = self.busq = TextCtrl(pListado, -1, "", (100, 50), (200, 25))
        l_dni = StaticText(pListado, -1, "CODIGO DE BARRA")
        dni = self.dni = TextCtrl(pListado, -1, "", (100, 50), (200, 25))
        dni.Bind(EVT_CHAR,self.error)
        l_nomyape = StaticText(pListado, -1, "DESCRIPCION")
        nomyape = self.nomyape = TextCtrl(pListado, -1, "", (100, 50), (300, 25))
        nomyape.Bind(EVT_CHAR,self.error0)
        l_list = StaticText(pListado, -1, "CODIGO")
        list = self.list = TextCtrl(pListado, -1, "", (100, 50), (200, 250))
        list.Bind(EVT_CHAR,self.error)
        l_nac = StaticText(pListado, -1, "PRECIO")
        nac = self.nac = TextCtrl(pListado, -1, "", )
        nac.Bind(EVT_CHAR,self.error)
        l_dire = StaticText(pListado, -1, "PROVEEDOR")
        dire = self.dire = TextCtrl(pListado, -1, "", (100, 50), (300, 25))
        dire.Bind(EVT_CHAR,self.error0)
        l_nuevo = StaticText(pListado, -1, "COSTO")
        nuevo = self.nuevo = TextCtrl(pListado, -1, "")
        nuevo.Bind(EVT_CHAR,self.error)
        l_foto = StaticText(pListado, -1, "FOTO")
        foto = self.foto = TextCtrl(pListado, -1, "", (100, 50), (200, 200))
        l_tel = StaticText(pListado, -1, "UTLIDAD")
        tel = self.tel = TextCtrl(pListado, -1, "")
        tel.Bind(EVT_CHAR,self.error)
        l_correo = StaticText(pListado, -1, "STOCK")
        correo = self.correo = TextCtrl(pListado, -1, "")
        correo.Bind(EVT_CHAR,self.error)
        l_stock = StaticText(pListado, -1, "MINIMO")
        stock = self.stock = TextCtrl(pListado, -1, "")
        stock.Bind(EVT_CHAR,self.error)
        l_marca = StaticText(pListado, -1, "MARCA")
        marca = self.marca = TextCtrl(pListado, -1, "")
        marca.Bind(EVT_CHAR,self.error0)
    # UBICACIONES
        #grilla1.Add(l_busq, pos=(1, 0))
        #grilla1.Add(busq, pos=(2, 0))
        grilla1.Add(l_dni, pos=(1, 0))
        grilla1.Add(dni, pos=(2, 0))
        grilla1.Add(l_nomyape, pos=(1, 2))
        grilla1.Add(nomyape, pos=(2, 2))
        grilla2.Add(l_list, pos=(1, 0))
        grilla2.Add(list, pos=(2, 0), span=(10, 0))
        grilla2.Add(l_nac, pos=(1, 1))
        grilla2.Add(nac, pos=(2, 1))
        grilla2.Add(l_dire, pos=(1, 2))
        grilla2.Add(dire, pos=(2, 2))
        grilla2.Add(l_nuevo, pos=(1, 3))
        grilla2.Add(nuevo, pos=(2, 3))
        grilla2.Add(l_foto, pos=(1, 4))
        grilla2.Add(foto, pos=(2, 4), span=(10, 5))
        grilla2.Add(l_tel, pos=(3, 1))
        grilla2.Add(tel, pos=(4, 1))
        grilla2.Add(l_correo, pos=(5, 1))
        grilla2.Add(correo, pos=(6, 1))
        grilla2.Add(l_stock, pos=(7, 1))
        grilla2.Add(stock, pos=(8, 1))
        grilla2.Add(l_marca, pos=(3, 2))
        grilla2.Add(marca, pos=(4, 2))
        #grilla3.Add(BotNuevo, pos=(0, 1))
        #grilla3.Add(BotEditar, pos=(0, 2))
        #grilla3.Add(BotBorrar, pos=(0, 3))
        grilla3.Add(BotCancelar, pos=(0, 19), span=(1, 1))
        grilla3.Add(BotAceptar, pos=(0, 21), span=(1, 1))

        pListado.SetSizer(BOX)
        fListado.Show()

    def CargarDatos (self, evt):
        self.fListado.Close()
        codi = self.codi = self.list.GetValue()
        desc = self.desc = self.nomyape.GetValue()
        marc = self.marc = self.marca.GetValue()
        cost = self.cost = self.nuevo.GetValue()
        precio = self.precio = self.nac.GetValue()
        stoc = self.stoc = self.correo.GetValue()
        self.dvlc.AppendItem([codi, desc, marc, cost, precio, stoc])
        self.Art = self.dvlc.AppendItem([codi, desc, marc, cost, precio, stoc])
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        lala = "INSERT INTO Articulos (Codigo, Descripcion, Marca, Costo, Precio, Stock)" \
               "VALUES ('" + codi + "','" + desc + "','" + marc + "','" + cost + "','" + precio + "','" + stoc + "')"
        cur.execute(lala)
        con.commit()
        con.close()

    def EditarArt (self, evt):
        colum = self.dvlc.GetSelectedRow()
        a = self.dvlc.GetValue(colum, 0)
        b = self.dvlc.GetValue(colum, 1)
        c = self.dvlc.GetValue(colum, 2)
        d = self.dvlc.GetValue(colum, 3)
        e = self.dvlc.GetValue(colum, 4)
        f = self.dvlc.GetValue(colum, 5)

        fListado = self.fListado = Frame(None, -1, "Sistema administrativo - CREAR ARTICULO", size=(1500, 900))
        fListado.SetBackgroundColour(WHITE)
        pListado = Panel(fListado)  # LE METO EL PANEL
        BOX = BoxSizer(VERTICAL)
        # Grillas
        grilla1 = GridBagSizer(10, 10)
        grilla2 = GridBagSizer(10, 30)
        grilla3 = GridBagSizer(10, 10)
        grilla4 = GridBagSizer(10, 10)
        BOX.Add(grilla1)
        BOX.Add(grilla2)
        BOX.Add(grilla3)
        BOX.Add(grilla4)
        # Botones
        BotNuevo = self.BotNuevo = Button(pListado, -1, "NUEVO", size=(100, 50))
        BotNuevo.SetBackgroundColour(WHITE)
        BotEditar = self.BotEditar = Button(pListado, -1, "EDITAR", size=(100, 50))
        BotEditar.SetBackgroundColour(WHITE)
        BotBorrar = self.BotBorrar = Button(pListado, -1, "BORRAR", size=(100, 50))
        BotBorrar.SetBackgroundColour(WHITE)
        jpeg = Bitmap('cancelar.bmp', BITMAP_TYPE_BMP)
        BotCancelar = self.bmpbtn = BitmapButton(pListado, -1, jpeg)
        jpeg = Bitmap('aceptar.bmp', BITMAP_TYPE_BMP)
        BotAceptar = self.bmpbtn1 = BitmapButton(pListado, -1, jpeg)
        BotAceptar.Bind(EVT_BUTTON, self.CargarDatos)
        # TEXTOS ESTATITOS Y CAJAS DE TEXTOS
        l_busq = StaticText(pListado, -1, "BUSQUEDA")
        busq = self.busq = TextCtrl(pListado, -1, "", (100, 50), (200, 25))

        l_dni = StaticText(pListado, -1, "CODIGO DE BARRA")
        dni = self.dni = TextCtrl(pListado, -1, "")
        dni.Bind(EVT_CHAR,self.error)
        l_nomyape = StaticText(pListado, -1, "DESCRIPCION")
        nomyape = self.nomyape = TextCtrl(pListado, -1, b, (100, 50), (300, 25))
        nomyape.Bind(EVT_CHAR,self.error0)
        l_list = StaticText(pListado, -1, "CODIGO")
        list = self.list = TextCtrl(pListado, -1, a, (100, 50), (200, 250))
        list.Bind(EVT_CHAR,self.error)
        l_nac = StaticText(pListado, -1, "PRECIO")
        nac = self.nac = TextCtrl(pListado, -1, e)
        nac.Bind(EVT_CHAR,self.error)
        l_dire = StaticText(pListado, -1, "PROVEEDOR")
        dire = self.dire = TextCtrl(pListado, -1, "", (100, 50), (300, 25))
        dire.Bind(EVT_CHAR,self.error0)
        l_nuevo = StaticText(pListado, -1, "COSTO")
        nuevo = self.nuevo = TextCtrl(pListado, -1, d)
        nuevo.Bind(EVT_CHAR,self.error)
        l_foto = StaticText(pListado, -1, "FOTO")
        foto = self.foto = TextCtrl(pListado, -1, "", (100, 50), (200, 200))
        l_tel = StaticText(pListado, -1, "UTLIDAD")
        tel = self.tel = TextCtrl(pListado, -1, "")
        tel.Bind(EVT_CHAR,self.error)
        l_correo = StaticText(pListado, -1, "STOCK")
        correo = self.correo = TextCtrl(pListado, -1, f)
        correo.Bind(EVT_CHAR,self.error)
        l_stock = StaticText(pListado, -1, "MINIMO")
        stock = self.stock = TextCtrl(pListado, -1, "")
        stock.Bind(EVT_CHAR,self.error)
        l_marca = StaticText(pListado, -1, "MARCA")
        marca = self.marca = TextCtrl(pListado, -1, c)
        marca.Bind(EVT_CHAR,self.error)
        # UBICACIONES
        grilla1.Add(l_busq, pos=(1, 0))
        grilla1.Add(busq, pos=(2, 0))
        grilla1.Add(l_dni, pos=(1, 2))
        grilla1.Add(dni, pos=(2, 2))
        grilla1.Add(l_nomyape, pos=(1, 4))
        grilla1.Add(nomyape, pos=(2, 4))
        grilla2.Add(l_list, pos=(1, 0))
        grilla2.Add(list, pos=(2, 0), span=(10, 0))
        grilla2.Add(l_nac, pos=(1, 1))
        grilla2.Add(nac, pos=(2, 1))
        grilla2.Add(l_dire, pos=(1, 2))
        grilla2.Add(dire, pos=(2, 2))
        grilla2.Add(l_nuevo, pos=(1, 3))
        grilla2.Add(nuevo, pos=(2, 3))
        grilla2.Add(l_foto, pos=(1, 4))
        grilla2.Add(foto, pos=(2, 4), span=(10, 5))
        grilla2.Add(l_tel, pos=(3, 1))
        grilla2.Add(tel, pos=(4, 1))
        grilla2.Add(l_correo, pos=(5, 1))
        grilla2.Add(correo, pos=(6, 1))
        grilla2.Add(l_stock, pos=(7, 1))
        grilla2.Add(stock, pos=(8, 1))
        grilla2.Add(l_marca, pos=(3, 2))
        grilla2.Add(marca, pos=(4, 2))
        grilla3.Add(BotNuevo, pos=(0, 1))
        grilla3.Add(BotEditar, pos=(0, 2))
        grilla3.Add(BotBorrar, pos=(0, 3))
        grilla3.Add(BotCancelar, pos=(0, 30), span=(1, 1))
        grilla3.Add(BotAceptar, pos=(0, 32), span=(1, 1))

        self.dvlc.DeleteItem(colum)  ##Eliminar Columna
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        sentencia = "DELETE FROM Articulos WHERE ID=" + str(colum+1)
        cur.execute(sentencia)
        con.commit()
        con.close()

        pListado.SetSizer(BOX)
        fListado.Show()
        return True



    def BorrarArt(self, evt):
        colum = self.dvlc.GetSelectedRow()  ##Devuelve la columna seleccionada por el usuario
        self.dvlc.DeleteItem(colum)  ##Eliminar Columna
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        sentencia = "DELETE FROM Articulos WHERE ID=" + str(colum+1)
        cur.execute(sentencia)
        con.commit()
        con.close()

    def cargarBDART (self, evt):
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        cur.execute("SELECT * FROM Articulos")
        ROWS = cur.fetchall()
        for ROW in ROWS:
            self.dvlc.AppendItem([ROW[1], ROW[2], ROW[3], ROW[4], ROW[5], ROW[6]])
        con.close()

    def cargarBDARTStock (self, evt):
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        cur.execute("SELECT * FROM Articulos")
        ROWS = cur.fetchall()
        for ROW in ROWS:
            if ROW[6] > "0":
                self.dvlc.AppendItem([ROW[1], ROW[2], ROW[3], ROW[4], ROW[5], ROW[6]])
        con.close()

    def cargarBDARTSinStock (self, evt):
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        cur.execute("SELECT * FROM Articulos")
        ROWS = cur.fetchall()
        for ROW in ROWS:
            if ROW[6] <= "0":
                self.dvlc.AppendItem([ROW[1], ROW[2], ROW[3], ROW[4], ROW[5], ROW[6]])
        con.close()

    def cargarBDARTStockMenosA (self, evt):
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        cur.execute("SELECT * FROM Articulos")
        ROWS = cur.fetchall()
        menosA = self.numero.GetValue()
        for ROW in ROWS:
            if ROW[6] < str(menosA):
                self.dvlc.AppendItem([ROW[1], ROW[2], ROW[3], ROW[4], ROW[5], ROW[6]])
        con.close()

    def BusquedaArt (self, evt):
        arti = self.arti = self.op.GetStringSelection()
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        sentencia = "SELECT * FROM Articulos WHERE Descripcion ='" + self.arti + "'"
        cur.execute(sentencia)
        ROWS = cur.fetchall()
        for ROW in ROWS:
            if ROW[2] == self.arti:
                self.dvlc.AppendItem([ROW[1], self.arti, ROW[3],ROW[4],ROW[5],ROW[6]])

# FRAME DE CLIENTES
    def clientes(self, evt):
        fClientes = self.Frame = Frame(None, -1, "CLIENTES", pos=(0, 0), size=(1500, 900))
        pClientes = self.pArticulo = Panel(fClientes)
        #fClientes.SetBackgroundColour(colour=(0, 255, 255))
        dvlc = self.dvlc = DataViewListCtrl(pClientes, size=(1050, 400))
        encabezado = [('ID CLIENTE', 150), ('NOMBRE Y APELLIDO', 150), ('DNI', 100), ('DIRECCION', 100),
                      ('FECHA DE NAC.', 150),
                      ('TELEFONO', 100), ('CORREO ELECTRONICO', 150), ('ESTADO DE CUENTA', 150)]
        for enca in encabezado:
            dvlc.AppendTextColumn(enca[0], width=enca[1])
        Box = BoxSizer(VERTICAL)

        # GRILLAS
        grilla1 = GridBagSizer(10, 10)
        grilla2 = GridBagSizer(10, 10)
        grilla3 = GridBagSizer(10, 10)
        Box.Add(grilla1)
        Box.Add(grilla2)
        Box.Add(grilla3)

        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        cur.execute("SELECT * FROM Clientes")
        ROWS = cur.fetchall()
        for ROW in ROWS:
            self.listaCli.append(ROW[2])
        con.close()

        self.op1 = Choice(pClientes, -1, (100, 50), choices=self.listaCli, size=(400, 25))

        # BOTONES
        BotBusqueda = self.BotBusqueda = Button(pClientes, -1, "BUSQUEDA", size=(100, 50))
        BotBusqueda.SetBackgroundColour(WHITE)
        BotBusqueda.Bind(EVT_BUTTON, self.BusquedaCli)
        BotTodos = self.BotTodos = Button(pClientes, -1, "TODOS", size=(100, 50))
        BotTodos.SetBackgroundColour(WHITE)
        BotTodos.Bind(EVT_BUTTON, self.cargarBDCLI)
        BotCuentaPos = self.BotCuentaPos = Button(pClientes, -1, "CUENTA POS.", size=(100, 50))
        BotCuentaPos.SetBackgroundColour(WHITE)
        BotCuentaNeg = self.BotCuentaNeg = Button(pClientes, -1, "CUENTA NEG.", size=(100, 50))
        BotCuentaNeg.SetBackgroundColour(WHITE)
        BotNuevo = self.BotStock = Button(pClientes, -1, "NUEVO", size=(100, 50))
        BotNuevo.SetBackgroundColour(WHITE)
        BotNuevo.Bind(EVT_BUTTON, self.ClienteNuevo)
        BotEditar = self.BotBusqueda = Button(pClientes, -1, "EDITAR", size=(100, 50))
        BotEditar.SetBackgroundColour(WHITE)
        BotEditar.Bind(EVT_BUTTON, self.EditarCli)
        BotBorrar = self.BotTodos = Button(pClientes, -1, "BORRAR", size=(100, 50))
        BotBorrar.SetBackgroundColour(WHITE)
        BotBorrar.Bind(EVT_BUTTON, self.BorrarCliente)
        #BotCancelar = self.BotBusqueda = Button(pClientes, -1, "CANCELAR", size=(100, 50))
        #BotCancelar.SetBackgroundColour(WHITE)
        #BotAceptar = self.BotTodos = Button(pClientes, -1, "ACEPTAR", size=(100, 50))
        #BotAceptar.SetBackgroundColour(WHITE)

        grilla1.Add(BotBusqueda, pos=(1, 0))
        grilla1.Add(self.op1, pos=(1, 1))
        grilla2.Add(self.dvlc, pos=(1, 0), span=(4, 5))  # depende los cuadros es la cantidad del numero
        grilla2.Add(BotTodos, pos=(1, 7))
        grilla2.Add(BotCuentaPos, pos=(2, 7))
        grilla2.Add(BotCuentaNeg, pos=(3, 7))
        grilla3.Add(BotNuevo, pos=(1, 0))
        grilla3.Add(BotEditar, pos=(1, 1))
        grilla3.Add(BotBorrar, pos=(1, 2))
        #grilla3.Add(BotCancelar, pos=(1, 35))
        #grilla3.Add(BotAceptar, pos=(1, 36))

        pClientes.SetSizer(Box)
        fClientes.Show()

    def ClienteNuevo(self, evt):
        fcn = self.fcn = Frame(None, -1, "Sistema administrativo - CREAR CLIENTE", size=(1500, 900))
        fcn.SetBackgroundColour(WHITE)
        pcn = Panel(fcn)  # LE METO EL PANEL
        BOX = BoxSizer(VERTICAL)
        # Grillas
        grilla1 = GridBagSizer(10, 10)
        grilla2 = GridBagSizer(10, 10)
        grilla3 = GridBagSizer(10, 10)
        grilla4 = GridBagSizer(10, 10)
        BOX.Add(grilla1)
        BOX.Add(grilla2)
        BOX.Add(grilla3)
        BOX.Add(grilla4)
        jpeg = Bitmap('cancelar.bmp', BITMAP_TYPE_BMP)
        BotCancelar = self.bmpbtn = BitmapButton(pcn, -1, jpeg, size=(150,70))
        jpeg = Bitmap('aceptar.bmp', BITMAP_TYPE_BMP)
        BotAceptar = self.bmpbtn1 = BitmapButton(pcn, -1, jpeg,size=(150,70))
        BotAceptar.Bind(EVT_BUTTON, self.CargarCli)
        l_nomyape = StaticText(pcn, -1, "NOMBRE Y APELLIDO")
        nomyape = self.nomyape = TextCtrl(pcn, -1, "", (100, 50), (340, 25))
        nomyape.Bind(EVT_CHAR,self.error0)
        l_list = StaticText(pcn, -1, " CODIGO")
        list = self.list = TextCtrl(pcn, -1, "", (100, 50), (200, 250))
        list.Bind(EVT_CHAR,self.error)
        l_nac = StaticText(pcn, -1, "DIRECCION")
        nac = self.nac = TextCtrl(pcn, -1, "", )
        l_dire = StaticText(pcn, -1, "CORREO ELECTRONICO")
        dire = self.dire = TextCtrl(pcn, -1, "", (100, 50), (300, 25))
        l_nuevo = StaticText(pcn, -1, "TELEFONO")
        nuevo = self.nuevo = TextCtrl(pcn, -1, "")
        nuevo.Bind(EVT_CHAR,self.error)
        l_foto = StaticText(pcn, -1, "FOTO")
        foto = self.foto = TextCtrl(pcn, -1, "", (100, 50), (200, 200))
        l_tel = StaticText(pcn, -1, "FECHA DE NACIMIENTO")
        tel = self.tel = TextCtrl(pcn, -1, "00/0/0000")
        l_cuenta = StaticText(pcn, -1, "ESTADO DE CUENTA")
        cuenta = self.cuenta = TextCtrl(pcn, -1, "")
        cuenta.Bind(EVT_CHAR,self.error)
        l_dni = StaticText(pcn, -1, "DNI")
        dni = self.correo = TextCtrl(pcn, -1, "")
        dni.Bind(EVT_CHAR,self.error)
# UBICACIONES
        #grilla1.Add(l_busq, pos=(1, 0))
        #grilla1.Add(busq, pos=(2, 0))
        #grilla1.Add(l_id, pos=(1, 2))
        #grilla1.Add(id, pos=(2, 2))
        grilla1.Add(l_nomyape, pos=(1, 0))
        grilla1.Add(nomyape, pos=(2, 0))
        grilla2.Add(l_list, pos=(1, 0))
        grilla2.Add(list, pos=(2, 0), span=(10, 0))
        grilla2.Add(l_nac, pos=(1, 2))
        grilla2.Add(nac, pos=(2, 2))
        grilla2.Add(l_dire, pos=(1, 4))
        grilla2.Add(dire, pos=(2, 4))
        grilla2.Add(l_nuevo, pos=(1, 6))
        grilla2.Add(nuevo, pos=(2, 6))
        grilla2.Add(l_foto, pos=(1, 8))
        grilla2.Add(foto, pos=(2, 8), span=(10, 5))
        grilla2.Add(l_tel, pos=(3, 2))
        grilla2.Add(tel, pos=(4, 2))
        grilla2.Add(l_cuenta, pos=(5, 2))
        grilla2.Add(cuenta, pos=(6, 2), span=(0, 0))
        grilla2.Add(l_dni, pos=(7, 2))
        grilla2.Add(dni, pos=(8, 2))
        #grilla3.Add(BotNuevo, pos=(0, 1))
        #grilla3.Add(BotEditar, pos=(0, 2))
        #grilla3.Add(BotBorrar, pos=(0, 3))
        grilla3.Add(BotCancelar, pos=(0, 20), span=(1, 1))
        grilla3.Add(BotAceptar, pos=(0, 22), span=(1, 1))
        pcn.SetSizer(BOX)
        fcn.Show()

    def cargarBDCLI (self, evt):
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        cur.execute("SELECT * FROM Clientes")
        ROWS = cur.fetchall()
        for ROW in ROWS:
            self.dvlc.AppendItem([ROW[1], ROW[2], ROW[3], ROW[4], ROW[5], ROW[6], ROW[7], ROW[8]])
            #self.lista.append(ROW[2])
        con.close()

    def CargarCli (self, evt):
        self.fcn.Close()
        codi = self.list.GetValue()
        desc = self.nomyape.GetValue()
        marc = self.correo.GetValue()
        cat = self.nac.GetValue()
        cost = self.tel.GetValue()
        uti = self.nuevo.GetValue()
        stoc = self.dire.GetValue()
        cuent = self.cuenta.GetValue()
        self.dvlc.AppendItem([codi, desc, marc, cat, cost, uti, stoc, cuent])
        #self.lista.append(desc)
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        lala = "INSERT INTO Clientes (Codigo, Nombre,  DNI, Direccion, Nacimiento, Telefono, Correo, Cuenta) " \
               "VALUES ('" + codi + "','" + desc + "','" + marc + "','" + cat + "','" + cost + "','" + uti + "','" + stoc + "','" + cuent + "')"
        cur.execute(lala)
        con.commit()
        con.close()

    def EditarCli (self,evt):



        colum = self.dvlc.GetSelectedRow()
        a = self.dvlc.GetValue(colum, 0)
        b = self.dvlc.GetValue(colum, 1)
        c = self.dvlc.GetValue(colum, 2)
        d = self.dvlc.GetValue(colum, 3)
        e = self.dvlc.GetValue(colum, 4)
        f = self.dvlc.GetValue(colum, 5)
        g = self.dvlc.GetValue(colum, 6)
        h = self.dvlc.GetValue(colum, 7)

        fcn = self.fcn = Frame(None, -1, "Sistema administrativo - CREAR CLIENTE", size=(1500, 900))
        fcn.SetBackgroundColour(WHITE)
        pcn = Panel(fcn)  # LE METO EL PANEL
        BOX = BoxSizer(VERTICAL)
    # Grillas
        grilla1 = GridBagSizer(10, 10)
        grilla2 = GridBagSizer(10, 10)
        grilla3 = GridBagSizer(10, 10)
        grilla4 = GridBagSizer(10, 10)
        BOX.Add(grilla1)
        BOX.Add(grilla2)
        BOX.Add(grilla3)
        BOX.Add(grilla4)
    # Botones
        BotNuevo = self.BotNuevo = Button(pcn, -1, "NUEVO", size=(100, 50))
        BotNuevo.SetBackgroundColour(WHITE)
        BotEditar = self.BotEditar = Button(pcn, -1, "EDITAR", size=(100, 50))
        BotEditar.SetBackgroundColour(WHITE)
        BotBorrar = self.BotBorrar = Button(pcn, -1, "BORRAR", size=(100, 50))
        BotBorrar.SetBackgroundColour(WHITE)
        jpeg = Bitmap('cancelar.bmp', BITMAP_TYPE_BMP)
        BotCancelar = self.bmpbtn = BitmapButton(pcn, -1, jpeg)
        jpeg = Bitmap('aceptar.bmp', BITMAP_TYPE_BMP)
        BotAceptar = self.bmpbtn1 = BitmapButton(pcn, -1, jpeg)
        BotAceptar.Bind(EVT_BUTTON, self.CargarCli)
    # TEXTOS ESTATITOS Y CAJAS DE TEXTOS
        l_busq = StaticText(pcn, -1, "BUSQUEDA")
        busq = self.busq = TextCtrl(pcn, -1, "", (100, 50), (200, 25))
        l_id = StaticText(pcn, -1, "ID CLIENTE")
        id = self.id = TextCtrl(pcn, -1, "")
        l_nomyape = StaticText(pcn, -1, "NOMBRE Y APELLIDO")
        nomyape = self.nomyape = TextCtrl(pcn, -1, b, (100, 50), (300, 25))
        l_list = StaticText(pcn, -1, " CODIGO")
        list = self.list = TextCtrl(pcn, -1, a, (100, 50), (200, 250))
        l_nac = StaticText(pcn, -1, "DIRECCION")
        nac = self.nac = TextCtrl(pcn, -1, d)
        l_dire = StaticText(pcn, -1, "CORREO ELECTRONICO")
        dire = self.dire = TextCtrl(pcn, -1, g, (100, 50), (300, 25))
        l_nuevo = StaticText(pcn, -1, "TELEFONO")
        nuevo = self.nuevo = TextCtrl(pcn, -1, f)
        l_foto = StaticText(pcn, -1, "FOTO")
        foto = self.foto = TextCtrl(pcn, -1, "", (100, 50), (200, 200))
        l_tel = StaticText(pcn, -1, "FECHA DE NACIMIENTO")
        tel = self.tel = TextCtrl(pcn, -1, e)
        l_cuenta = StaticText(pcn, -1, "ESTADO DE CUENTA")
        cuenta = self.cuenta = TextCtrl(pcn, -1, h)
        l_dni = StaticText(pcn, -1, "DNI")
        dni = self.correo = TextCtrl(pcn, -1, c)
    # UBICACIONES
        grilla1.Add(l_busq, pos=(1, 0))
        grilla1.Add(busq, pos=(2, 0))
        grilla1.Add(l_id, pos=(1, 2))
        grilla1.Add(id, pos=(2, 2))
        grilla1.Add(l_nomyape, pos=(1, 5))
        grilla1.Add(nomyape, pos=(2, 5))
        grilla2.Add(l_list, pos=(1, 0))
        grilla2.Add(list, pos=(2, 0), span=(10, 0))
        grilla2.Add(l_nac, pos=(1, 2))
        grilla2.Add(nac, pos=(2, 2))
        grilla2.Add(l_dire, pos=(1, 4))
        grilla2.Add(dire, pos=(2, 4))
        grilla2.Add(l_nuevo, pos=(1, 6))
        grilla2.Add(nuevo, pos=(2, 6))
        grilla2.Add(l_foto, pos=(1, 8))
        grilla2.Add(foto, pos=(2, 8), span=(10, 5))
        grilla2.Add(l_tel, pos=(3, 2))
        grilla2.Add(tel, pos=(4, 2))
        grilla2.Add(l_cuenta, pos=(5, 2))
        grilla2.Add(cuenta, pos=(6, 2), span=(0, 0))
        grilla2.Add(l_dni, pos=(7, 2))
        grilla2.Add(dni, pos=(8, 2))
        grilla3.Add(BotNuevo, pos=(0, 1))
        grilla3.Add(BotEditar, pos=(0, 2))
        grilla3.Add(BotBorrar, pos=(0, 3))
        grilla3.Add(BotCancelar, pos=(0, 30), span=(1, 1))
        grilla3.Add(BotAceptar, pos=(0, 32), span=(1, 1))

        self.dvlc.DeleteItem(colum)  ##Eliminar Columna
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        sentencia = "DELETE FROM Clientes WHERE ID=" + str(colum+1)
        cur.execute(sentencia)
        con.commit()
        con.close()

        pcn.SetSizer(BOX)
        fcn.Show()

    def BorrarCliente(self, evt):
        colum = self.dvlc.GetSelectedRow()  ##Devuelve la columna seleccionada por el usuario
        self.dvlc.DeleteItem(colum)  ##Eliminar Columna
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        sentencia = "DELETE FROM Clientes WHERE ID=" + str(colum+1)
        cur.execute(sentencia)
        con.commit()
        con.close()

    def BusquedaCli (self, evt):
        clie = self.clie = self.op1.GetStringSelection()
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        sentencia = "SELECT * FROM Clientes WHERE Nombre ='" + self.clie + "'"
        cur.execute(sentencia)
        ROWS = cur.fetchall()
        for ROW in ROWS:
            if ROW[2] == self.clie:
                self.dvlc.AppendItem([ROW[1], self.clie, ROW[3],ROW[4],ROW[5],ROW[6],ROW[7],ROW[8]])

# FRAME DE PROVEEDORES
    def Proveedores(self, evt):
        fProveedores = self.Frame = Frame(None, -1, "Proveedores", pos=(0, 0), size=(1000, 900))
        pProveedores = self.pProveedores = Panel(fProveedores)
        # fClientes.SetBackgroundColour(colour=(0, 255, 255))
        dvlc = self.dvlc = DataViewListCtrl(pProveedores, size=(650, 400))
        encabezado = [('ID PROVEEDOR', 150), ('DESCRIPCION', 150), ('DIRECCION', 100),
                      ('TELEFONO', 100), ('CORREO ELECTRONICO', 150)]
        for enca in encabezado:
            dvlc.AppendTextColumn(enca[0], width=enca[1])
        Box = BoxSizer(VERTICAL)
# GRILLAS
        grilla1 = GridBagSizer(10, 10)
        grilla2 = GridBagSizer(10, 10)
        grilla3 = GridBagSizer(10, 10)
        Box.Add(grilla1)
        Box.Add(grilla2)
        Box.Add(grilla3)

        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        cur.execute("SELECT * FROM Proveedores")
        ROWS = cur.fetchall()
        for ROW in ROWS:
            self.listaProveedores.append(ROW[2])
        con.close()

        # BOTONES
        BotBusqueda = self.BotBusqueda = Button(pProveedores, -1, "BUSQUEDA", size=(100, 50))
        BotBusqueda.SetBackgroundColour(WHITE)
        BotBusqueda.Bind(EVT_BUTTON, self.BusquedaPro)
        #BotTodos = self.BotTodos = Button(pProveedores, -1, "LISTA DE PRECIOS", size=(150, 100))
        #BotTodos.SetBackgroundColour(WHITE)
        #BotTodos.Bind(EVT_BUTTON, self.listaPrecios)
        BotNuevo = self.BotStock = Button(pProveedores, -1, "NUEVO", size=(100, 50))
        BotNuevo.SetBackgroundColour(WHITE)
        BotNuevo.Bind(EVT_BUTTON, self.ProveedorNuevo)
        BotEditar = self.BotBusqueda = Button(pProveedores, -1, "EDITAR", size=(100, 50))
        BotEditar.SetBackgroundColour(WHITE)
        BotEditar.Bind(EVT_BUTTON, self.EditarPro)
        BotBorrar = self.BotTodos = Button(pProveedores, -1, "BORRAR", size=(100, 50))
        BotBorrar.SetBackgroundColour(WHITE)
        BotBorrar.Bind(EVT_BUTTON, self.BorrarProveedor)
        BotCargar = self.BotCargar = Button(pProveedores, -1, "CARGAR", size=(100, 50))
        BotCargar.SetBackgroundColour(WHITE)
        BotCargar.Bind(EVT_BUTTON, self.cargarBDPRO)
        #BotCancelar = self.BotBusqueda = Button(pProveedores, -1, "CANCELAR", size=(100, 50))
        #BotCancelar.SetBackgroundColour(WHITE)
        #BotAceptar = self.BotTodos = Button(pProveedores, -1, "ACEPTAR", size=(100, 50))
        #BotAceptar.SetBackgroundColour(WHITE)
        self.Proveedor = Choice(pProveedores, -1, (100, 50), choices=self.listaProveedores, size=(400, 25))
        # Codigo - Caja de Texto
        #codigo = self.codigo = TextCtrl(pProveedores, -1, "Codigo", (100, 50), (50, 49))
        # Nombre - Caja de Texto
        #nombre = self.nombre = TextCtrl(pProveedores, -1, "Descripcion", (100, 50), (400, 49))
        grilla1.Add(BotBusqueda, pos=(1, 0))
        grilla1.Add(self.Proveedor, pos=(1, 1))
        #grilla1.Add(nombre, pos=(1, 2))
        grilla2.Add(self.dvlc, pos=(1, 0), span=(4, 5))  # depende los cuadros es la cantidad del numero
        #grilla2.Add(BotTodos, pos=(1, 7))
        grilla3.Add(BotNuevo, pos=(1, 0))
        grilla3.Add(BotEditar, pos=(1, 1))
        grilla3.Add(BotBorrar, pos=(1, 2))
        grilla3.Add(BotCargar, pos=(1, 4))
        #grilla3.Add(BotCancelar, pos=(1, 15))
        #grilla3.Add(BotAceptar, pos=(1, 16))

        pProveedores.SetSizer(Box)
        fProveedores.Show()

    def ProveedorNuevo(self, evt):
        fpn = self.fpn = Frame(None, -1, "Sistema administrativo - CREAR CLIENTE", size=(1500, 900))
        fpn.SetBackgroundColour(WHITE)
        ppn = Panel(fpn)  # LE METO EL PANEL
        BOX = BoxSizer(VERTICAL)
# Grillas
        grilla1 = GridBagSizer(10, 10)
        grilla2 = GridBagSizer(10, 10)
        grilla3 = GridBagSizer(10, 10)
        grilla4 = GridBagSizer(10, 10)
        BOX.Add(grilla1)
        BOX.Add(grilla2)
        BOX.Add(grilla3)
        BOX.Add(grilla4)
# Botones
        jpeg = Bitmap('cancelar.bmp', BITMAP_TYPE_BMP)
        BotCancelar = self.bmpbtn = BitmapButton(ppn, -1, jpeg,size=(150,70))
        jpeg = Bitmap('aceptar.bmp', BITMAP_TYPE_BMP)
        BotAceptar = self.bmpbtn1 = BitmapButton(ppn, -1, jpeg,size=(150,70))
        BotAceptar.Bind(EVT_BUTTON, self.CargarPro)
# TEXTOS ESTATITOS Y CAJAS DE TEXTOS
        l_desc = StaticText(ppn, -1, "DESCRIPCION")
        desc = self.desc = TextCtrl(ppn, -1, "", (100, 50), (340, 25))
        desc.Bind(EVT_CHAR,self.error0)
        l_codi = StaticText(ppn, -1, " CODIGO")
        codi = self.codi = TextCtrl(ppn, -1, "", (100, 50), (200, 250))
        codi.Bind(EVT_CHAR,self.error)
        l_dire = StaticText(ppn, -1, "DIRECCION")
        dire = self.dire = TextCtrl(ppn, -1, "", )
        dire.Bind(EVT_CHAR,self.error0)
        l_correo = StaticText(ppn, -1, "CORREO ELECTRONICO")
        correo = self.correo = TextCtrl(ppn, -1, "", (100, 50), (300, 25))
        l_tel = StaticText(ppn, -1, "TELEFONO")
        tel = self.tel = TextCtrl(ppn, -1, "")
        tel.Bind(EVT_CHAR,self.error)
        l_foto = StaticText(ppn, -1, "FOTO")
        foto = self.foto = TextCtrl(ppn, -1, "", (100, 50), (200, 200))

# UBICACIONES
        #grilla1.Add(l_busq, pos=(1, 0))
        #grilla1.Add(busq, pos=(2, 0))
        #grilla1.Add(l_id, pos=(1, 2))
        #grilla1.Add(id, pos=(2, 2))
        grilla1.Add(l_desc, pos=(1, 0))
        grilla1.Add(desc, pos=(2, 0))
        grilla2.Add(l_codi, pos=(1, 0))
        grilla2.Add(codi, pos=(2, 0), span=(10, 0))
        grilla2.Add(l_dire, pos=(1, 2))
        grilla2.Add(dire, pos=(2, 2))
        grilla2.Add(l_correo, pos=(1, 4))
        grilla2.Add(correo, pos=(2, 4))
        grilla2.Add(l_tel, pos=(1, 6))
        grilla2.Add(tel, pos=(2, 6))
        grilla2.Add(l_foto, pos=(1, 8))
        grilla2.Add(foto, pos=(2, 8), span=(10, 5))
        #grilla3.Add(BotNuevo, pos=(0, 1))
        #grilla3.Add(BotEditar, pos=(0, 2))
        #grilla3.Add(BotBorrar, pos=(0, 3))
        grilla3.Add(BotCancelar, pos=(0, 18), span=(1, 1))
        grilla3.Add(BotAceptar, pos=(0, 20), span=(1, 1))
        ppn.SetSizer(BOX)
        fpn.Show()

    def cargarBDPRO(self, evt):
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        cur.execute("SELECT * FROM Proveedores")
        ROWS = cur.fetchall()
        for ROW in ROWS:
            self.dvlc.AppendItem([ROW[1], ROW[2], ROW[3], ROW[4], ROW[5]])
        con.close()

    def CargarPro(self, evt):
        self.fpn.Close()
        codi = self.codi.GetValue()
        desc = self.desc.GetValue()
        dire = self.dire.GetValue()
        tel = self.tel.GetValue()
        corre = self.correo.GetValue()
        self.dvlc.AppendItem([codi, desc, dire, tel, corre])
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        lala = "INSERT INTO Proveedores (Codigo, Descripcion,  Direccion, Telefono, correo) " \
               "VALUES ('" + codi + "','" + desc + "','" + dire + "','" + tel + "','" + corre + "')"
        cur.execute(lala)
        con.commit()
        con.close()

    """def listaPrecios (self, evt):
        if self.provee == "TUBOS":
            con = sqlite3.connect("EFI_DB")
            cur = con.cursor()
            sentencia1 = "SELECT Id, Codigo, Descripcion, Costo, Stock FROM Tubos"
            cur.execute(sentencia1)
            for i in cur :
                print (i[0])
                print (i[1])
                print (i[2])
                print (i[3])
                print (i[4])
        con.close()"""

    def EditarPro (self, evt):




        colum = self.dvlc.GetSelectedRow()
        a = self.dvlc.GetValue(colum, 0)
        b = self.dvlc.GetValue(colum, 1)
        c = self.dvlc.GetValue(colum, 2)
        d = self.dvlc.GetValue(colum, 3)
        e = self.dvlc.GetValue(colum, 4)

        fpn = self.fpn = Frame(None, -1, "Sistema administrativo - EDITAR PROVEEDOR", size=(1500, 900))
        fpn.SetBackgroundColour(WHITE)
        ppn = Panel(fpn)  # LE METO EL PANEL
        BOX = BoxSizer(VERTICAL)
        # Grillas
        grilla1 = GridBagSizer(10, 10)
        grilla2 = GridBagSizer(10, 10)
        grilla3 = GridBagSizer(10, 10)
        grilla4 = GridBagSizer(10, 10)
        BOX.Add(grilla1)
        BOX.Add(grilla2)
        BOX.Add(grilla3)
        BOX.Add(grilla4)
        # Botones
        BotNuevo = self.BotNuevo = Button(ppn, -1, "NUEVO", size=(100, 50))
        BotNuevo.SetBackgroundColour(WHITE)
        BotEditar = self.BotEditar = Button(ppn, -1, "EDITAR", size=(100, 50))
        BotEditar.SetBackgroundColour(WHITE)
        BotBorrar = self.BotBorrar = Button(ppn, -1, "BORRAR", size=(100, 50))
        BotBorrar.SetBackgroundColour(WHITE)
        jpeg = Bitmap('cancelar.bmp', BITMAP_TYPE_BMP)
        BotCancelar = self.bmpbtn = BitmapButton(ppn, -1, jpeg)
        jpeg = Bitmap('aceptar.bmp', BITMAP_TYPE_BMP)
        BotAceptar = self.bmpbtn1 = BitmapButton(ppn, -1, jpeg)
        BotAceptar.Bind(EVT_BUTTON, self.CargarPro)
        # TEXTOS ESTATITOS Y CAJAS DE TEXTOS
        l_busq = StaticText(ppn, -1, "BUSQUEDA")
        busq = self.busq = TextCtrl(ppn, -1, "", (100, 50), (200, 25))
        l_id = StaticText(ppn, -1, "ID PROVEEDOR")
        id = self.id = TextCtrl(ppn, -1, "")
        l_desc = StaticText(ppn, -1, "DESCRIPCION")
        desc = self.desc = TextCtrl(ppn, -1, b, (100, 50), (300, 25))
        l_codi = StaticText(ppn, -1, " CODIGO")
        codi = self.codi = TextCtrl(ppn, -1, a, (100, 50), (200, 250))
        l_dire = StaticText(ppn, -1, "DIRECCION")
        dire = self.dire = TextCtrl(ppn, -1, c)
        l_correo = StaticText(ppn, -1, "CORREO ELECTRONICO")
        correo = self.correo = TextCtrl(ppn, -1, e, (100, 50), (300, 25))
        l_tel = StaticText(ppn, -1, "TELEFONO")
        tel = self.tel = TextCtrl(ppn, -1, d)
        l_foto = StaticText(ppn, -1, "FOTO")
        foto = self.foto = TextCtrl(ppn, -1, "", (100, 50), (200, 200))

        # UBICACIONES
        grilla1.Add(l_busq, pos=(1, 0))
        grilla1.Add(busq, pos=(2, 0))
        grilla1.Add(l_id, pos=(1, 2))
        grilla1.Add(id, pos=(2, 2))
        grilla1.Add(l_desc, pos=(1, 5))
        grilla1.Add(desc, pos=(2, 5))
        grilla2.Add(l_codi, pos=(1, 0))
        grilla2.Add(codi, pos=(2, 0), span=(10, 0))
        grilla2.Add(l_dire, pos=(1, 2))
        grilla2.Add(dire, pos=(2, 2))
        grilla2.Add(l_correo, pos=(1, 4))
        grilla2.Add(correo, pos=(2, 4))
        grilla2.Add(l_tel, pos=(1, 6))
        grilla2.Add(tel, pos=(2, 6))
        grilla2.Add(l_foto, pos=(1, 8))
        grilla2.Add(foto, pos=(2, 8), span=(10, 5))
        grilla3.Add(BotNuevo, pos=(0, 1))
        grilla3.Add(BotEditar, pos=(0, 2))
        grilla3.Add(BotBorrar, pos=(0, 3))
        grilla3.Add(BotCancelar, pos=(0, 30), span=(1, 1))
        grilla3.Add(BotAceptar, pos=(0, 32), span=(1, 1))

        self.dvlc.DeleteItem(colum)  ##Eliminar Columna
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        sentencia = "DELETE FROM Proveedores WHERE ID=" + str(colum + 1)
        cur.execute(sentencia)
        con.commit()
        con.close()

        ppn.SetSizer(BOX)
        fpn.Show()

    def BorrarProveedor(self, evt):
        colum = self.dvlc.GetSelectedRow()  ##Devuelve la columna seleccionada por el usuario
        self.dvlc.DeleteItem(colum)  ##Eliminar Columna
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        sentencia = "DELETE FROM Proveedores WHERE ID=" + str(colum + 1)
        cur.execute(sentencia)
        con.commit()
        con.close()

    def BusquedaPro (self, evt):
        provee = self.provee = self.Proveedor.GetStringSelection()
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        sentencia = "SELECT * FROM Proveedores WHERE Descripcion ='" + self.provee + "'"
        cur.execute(sentencia)
        ROWS = cur.fetchall()
        for ROW in ROWS:
            if ROW[2] == self.provee:
                self.dvlc.AppendItem([ROW[1], self.provee, ROW[3], ROW[4], ROW[5]])

#FUNCIONES POR FUERA DE LOS FRAMES
    def Examinar(self,evt):
        f4=Frame(None,-1,"SELECCIONE",size=(500,300))
        p4=self.p4=Panel(f4)
        self.buscararchivo= FileCtrl(self.p4, -1, defaultDirectory="",
                 defaultFilename="",wildCard=wx.FileSelectorDefaultWildcardStr,
                 style=wx.FC_OPEN,size=(600,600))
        f4.Show()
        return True

    def AcepOp(self,evt):
        self.NOMBRE=str(self.TextoNombre.GetValue())
        print (self.NOMBRE)

    def fbbCallback(self, evt):
        self.log.write('FileBrowseButton: %s\n' % evt.GetString())

# CAlENDARIO
    def abrirCal(self, evt):
        self.f3 = Frame(None, -1, "Calendario")
        g3 = BoxSizer()
        cal = CalendarCtrl(self.f3, -1, DateTime.Today())
        g3.Add(cal)
        cal.Bind(EVT_CALENDAR, self.OnCalSelected)
        self.f3.SetSizerAndFit(g3)
        self.f3.Show()

    def OnCalSelected(self, evt):
        # print('OnCalSelected: %s\n' % e.GetDate())
        hoy = self.hoy = str(evt.GetDate())
        hoy = self.hoy = hoy[3:5] + "/" + hoy[:2] + "/20" + hoy[6:8]
        self.f3.Show(False)
        self.fecha.SetValue(self.hoy)

#FUNCION PARA VENTAS Y CAJA
    def Cobrar(self,evt):
        can = self.can = int(self.CajaCantidad.GetValue())
        descuento = self.descuento = int((int(self.BotonDesc.GetValue()) * self.suma) / 100)
        paga = int(self.CajaPaga.GetValue())
        total = int(paga - self.suma + descuento)
        self.CajaVuelto.SetLabel(str(total))
        # STOCK
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        cur.execute("SELECT * FROM Articulos")  # WHERE Descripcion =" + self.descr
        ROWS = cur.fetchall()
        for ROW in ROWS:
            if ROW[2] == self.descr:
                # print ((int(ROW[6]))-self.can)
                dife = ((int(ROW[6])) - self.can)
                sentencia = "UPDATE Articulos SET Stock = " + str(dife) + " WHERE Descripcion ='" + self.descr + "'"
                cur.execute(sentencia)
        con.commit()
        con.close()

        cajerobd = self.Cajeros.GetValue()
        totaldb = self.suma
        DAY = str(DateTime.Today())
        fechabd = DAY[:-8]
        cliente = self.ch.GetStringSelection()
        producto = self.ch1.GetStringSelection()
        fdpagobd = self.rb.GetStringSelection()
        Desc = int(self.BotonDesc.GetValue())
        TmenosD = self.suma - (self.suma * Desc / 100)
        print(cajerobd, totaldb, fechabd, cliente, producto, fdpagobd, TmenosD)

        if fdpagobd == "EFECTIVO":
            con = sqlite3.connect("EFI_DB")
            cur = con.cursor()
            try:
                cur.execute("INSERT INTO Caja (Fecha,CajaN,Cliente,Efectivo,Tarjeta,Cuenta) VALUES(?,?,?,?,?,?)",
                            (fechabd, cajerobd, cliente, TmenosD, 0 , 0))
            except:
                print("algo no anda")

            con.commit()
            con.close()

        else:
            pass
        if fdpagobd == "TARJETA":
            con = sqlite3.connect("EFI_DB")
            cur = con.cursor()
            try:
                cur.execute("INSERT INTO Caja (Fecha,CajaN,Cliente,Efectivo,Tarjeta,Cuenta) VALUES(?,?,?,?,?,?)",
                            (fechabd, cajerobd, cliente, 0, TmenosD ,0))
            except:
                print("algo no anda")

            con.commit()
            con.close()
        else:
            pass

        if fdpagobd == "CUENTA CORRIENTE":
            con = sqlite3.connect("EFI_DB")
            cur = con.cursor()
            try:
                cur.execute("INSERT INTO Caja (Fecha,CajaN,Cliente,Efectivo,Tarjeta,Cuenta) VALUES(?,?,?,?,?,?)",
                            (fechabd, cajerobd, cliente,0,0, TmenosD))
            except:
                print("algo no anda")

            cli = self.ch.GetStringSelection()
            print(cli)

            cur.execute("SELECT * FROM Clientes")  # WHERE Descripcion =" + self.descr
            ROWS = cur.fetchall()
            for ROW in ROWS:
                if ROW[2] == cli:
                    dife = ((int(ROW[8])) - TmenosD)
                    sentencia = "UPDATE Clientes SET Cuenta = " + str(dife) + " WHERE Nombre ='" + cli + "'"
                    cur.execute(sentencia)
            con.commit()
            con.close()

        # ACA TENGO Q METER LA FUNCION PARA CC

        else:
            pass
        can = self.can = int(self.CajaCantidad.GetValue())
        descuento = self.descuento = int((int(self.BotonDesc.GetValue()) * self.suma) / 100)
        paga = int(self.CajaPaga.GetValue())
        total = int(paga - self.suma + descuento)
        self.CajaVuelto.SetLabel(str(total))
    # STOCK
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        cur.execute("SELECT * FROM Articulos")  # WHERE Descripcion =" + self.descr
        ROWS = cur.fetchall()
        for ROW in ROWS:
            if ROW[2] == self.descr:
                # print ((int(ROW[6]))-self.can)
                dife = ((int(ROW[6])) - self.can)
                sentencia = "UPDATE Articulos SET Stock = " + str(dife) + " WHERE Descripcion ='" + self.descr + "'"
                cur.execute(sentencia)
        con.commit()
        con.close()

        cajerobd = self.Cajeros.GetValue()
        totaldb = self.suma
        DAY = str(DateTime.Today())
        fechabd = DAY[:-8]
        cliente = self.ch.GetStringSelection()
        producto = self.ch1.GetStringSelection()
        fdpagobd = self.rb.GetStringSelection()
        Desc = int(self.BotonDesc.GetValue())
        TmenosD = self.suma - (self.suma * Desc / 100)
        print(cajerobd, totaldb, fechabd, cliente, producto, fdpagobd, TmenosD)

        """if fdpagobd == "EFECTIVO":
            con = sqlite3.connect("EFI_DB")
            cur = con.cursor()
            try:
                cur.execute("INSERT INTO Caja (Fecha,CajaN,Cliente,Efectivo) VALUES(?,?,?,?)",
                            (fechabd, cajerobd, cliente, TmenosD))
            except:
                print("algo no anda")

            con.commit()
            con.close()

        else:
            pass
        if fdpagobd == "TARJETA":
            con = sqlite3.connect("EFI_DB")
            cur = con.cursor()
            try:
                cur.execute("INSERT INTO Caja (Fecha,CajaN,Cliente,Tarjeta) VALUES(?,?,?,?)",
                            (fechabd, cajerobd, cliente, TmenosD))
            except:
                print("algo no anda")

            con.commit()
            con.close()
        else:
            pass

        if fdpagobd == "CUENTA CORRIENTE":
            con = sqlite3.connect("EFI_DB")
            cur = con.cursor()
            try:
                cur.execute("INSERT INTO Caja (Fecha,CajaN,Cliente,Cuenta) VALUES(?,?,?,?)",
                            (fechabd, cajerobd, cliente, TmenosD))
            except:
                print("algo no anda")

            cli = self.ch.GetStringSelection()
            print(cli)

            cur.execute("SELECT * FROM Clientes")  # WHERE Descripcion =" + self.descr
            ROWS = cur.fetchall()
            for ROW in ROWS:
                if ROW[2] == cli:
                    dife = ((int(ROW[8])) - TmenosD)
                    sentencia = "UPDATE Clientes SET Cuenta = " + str(dife) + " WHERE Nombre ='" + cli + "'"
                    cur.execute(sentencia)
            con.commit()
            con.close()

            # ACA TENGO Q METER LA FUNCION PARA CC

        else:
            pass"""



    def CargarDatosART (self,evt):
        can = self.can = int(self.CajaCantidad.GetValue())
        desc = self.descr = self.ch1.GetStringSelection()
        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        sentencia = "SELECT * FROM Articulos WHERE Descripcion ='" + self.descr + "'"
        cur.execute(sentencia)
        ROWS = cur.fetchall()
        for ROW in ROWS:
            if ROW[2] == self.descr:
                self.dvlc.AppendItem([ROW[1], self.descr, self.can, ROW[6], int(ROW[5])*self.can])
        self.suma=0
        for x in range(self.dvlc.GetItemCount()):
            self.suma = (int(self.suma)) + (int(self.dvlc.GetValue(x,4)))
            self.TextSuma.SetLabel(str(self.suma))
            self.suma=int(self.suma)

    def cerrarFac (self, event):
        self.fCartel.Close()
        self.f2.Close()

    def Cancelar(self,evt):
        #self.suma = 0
        for x in range(self.dvlc.GetItemCount()):
            self.dvlc.DeleteItem(0)
        self.TextSuma.SetLabel("0")
        self.CajaVuelto.SetLabel("0")

    def abrirurl(self,evt):
        webbrowser.open("www.linkedin.com/in/matiasjavierlucero")
        webbrowser.open("www.linkedin.com/in/francisco-garrione-ba3957171")

    def procesacaja(self,evt):
        inicial=self.inicial=int(self.cantIn.GetValue())
        CAJERO=self.CAJERO=self.Cajas.GetValue()
        self.ef=0
        self.tar=0
        self.cc=0
        DAY = str(DateTime.Today())
        self.fechabd = DAY[:-8]

        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM Caja")
            listacaja = self.listacaja = []
            ROWS = cur.fetchall()
            for ROW in ROWS:
                self.listacaja.append(ROW)

        except:
            print ("NO ANDA")

        for x in range(len(self.listacaja)):
            if self.listacaja[x][2]==self.CAJERO and self.listacaja[x][1]== self.fechabd:
                self.ef=self.ef+(float(self.listacaja[x][4]))
                self.efec.SetLabel(str(self.ef))

        for x in range(len(self.listacaja)):

            if self.listacaja[x][2]==self.CAJERO  and self.listacaja[x][1]==self.fechabd:
                self.tar=self.tar+(float(self.listacaja[x][5]))
                self.cred.SetLabel(str(self.tar))

        for x in range(len(self.listacaja)):
            if self.listacaja[x][2]==self.CAJERO  and self.listacaja[x][1]==self.fechabd:
                self.cc=self.cc+(float(self.listacaja[x][6]))
                self.deb.SetLabel(str(self.cc))

        tot=float(self.tar)+float(self.cc)+float(self.ef)+inicial
        self.total.SetLabel(str(tot))

        if self.CAJERO=="Todas" :
            con = sqlite3.connect("EFI_DB")
            cur = con.cursor()
            #try:
             #   cur.execute("CREATE TABLE CajasDiarias (Id INTEGER PRIMARY KEY, FECHA ,EFECTIVO,TARJETA,CuentaCorriente)")
            #except:
             #   pass

            for x in range(len(self.listacaja)):
                if self.listacaja[x][1]==self.fechabd:
                    self.ef = self.ef + (int(self.listacaja[x][4]))
                    self.efec.SetLabel(str(self.ef))
                    self.tar = self.tar + (int(self.listacaja[x][5]))
                    self.cred.SetLabel(str(self.tar))
                    self.cc = self.cc + (int(self.listacaja[x][6]))
                    self.deb.SetLabel(str(self.cc))

            tot = int(self.tar) + int(self.cc) + int(self.ef) + inicial
            self.total.SetLabel(str(tot))

            try:
                cur.execute("INSERT INTO CajasDiarias (FECHA,EFECTIVO,TARJETA,CuentaCorriente) VALUES (?,?,?,?)" ,(self.fechabd,self.ef,self.tar,self.cc))
            except:
                print ("ANDA MAL")

            con.commit()
            con.close()
        else:
            pass

    def cajafinal(self,evt):
        Fcaja=Frame(None,-1,"CAJAS DIARIAS",size=(700,401))
        Pcaja=Panel(Fcaja,-1)
        Cajasizer=BoxSizer(VERTICAL)
        GCaja=GridBagSizer(10,10)

        datalist = self.datalist = DataViewListCtrl(Pcaja, size=(450, 200))
        encabezado = [('Fecha', 100), ('Efectivo', 150), ('Tarjeta', 100), ('Cuenta Corriente', 100)]
        for enca in encabezado:
            datalist.AppendTextColumn(enca[0], width=enca[1])

        a=StaticText(Pcaja,-1,"LISTADO DE CAJAS DIARIAS")
        Cajasizer.Add(a)
        Cajasizer.Add(GCaja)
        GCaja.Add(datalist,pos=(1,1))

        Pcaja.SetSizer(Cajasizer)

        con = sqlite3.connect("EFI_DB")
        cur = con.cursor()

        cur.execute("SELECT * FROM CajasDiarias")
        rows = cur.fetchall()

        con.commit()
        con.close()

        self.listadecajas = []

        for row in rows:
            self.listadecajas.append(row)

        for x in range(len(self.listadecajas)):
            data = [self.listadecajas[x][1], self.listadecajas[x][2],self.listadecajas[x][3], self.listadecajas[x][4]]
            self.datalist.AppendItem(data)




        Fcaja.Show()
        return True

# CONTROL DE ERRORES
    def error(self,evt):
        if 48<=evt.GetKeyCode()<=57 or 0<=evt.GetKeyCode()<=32:
            evt.Skip()
        else:
            MessageBox("SOLO ADMITE NUMERO")

    def error0(self,evt):
        if 65<=evt.GetKeyCode()<=90 or 0<=evt.GetKeyCode()<=32:
            evt.Skip()
        else:
            MessageBox( "SOLO ADMITE MAYUSCULAS","NO SEA PAVO")

    def calculadora(self,etv):
        os.system('calc.exe')


a = MyApp()

a.MainLoop()
