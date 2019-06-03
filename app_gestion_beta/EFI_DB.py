#CREO LA TABLA EFI.DB Y LE METO LOS VALORES DE DVLC
import sqlite3
con = sqlite3.connect("EFI_DB")
cur = con.cursor()
try:
    cur.execute("CREATE TABLE Ternium (Id INTEGER PRIMARY KEY, Codigo TEXT, Descripcion TEXT, Costo TEXT, Stock TEXT)")
    cur.execute("CREATE TABLE Ortiz (Id INTEGER PRIMARY KEY, Codigo TEXT, Descripcion TEXT, Costo TEXT, Stock TEXT)")
    cur.execute("CREATE TABLE Tubos (Id INTEGER PRIMARY KEY, Codigo TEXT, Descripcion TEXT, Costo TEXT, Stock TEXT)")
    cur.execute("CREATE TABLE Articulos (Id INTEGER PRIMARY KEY, Codigo TEXT, Descripcion TEXT, Marca TEXT, Costo TEXT, Precio TEXT, Stock TEXT)")
    cur.execute("CREATE TABLE Clientes (Id INTEGER PRIMARY KEY, Codigo TEXT, Nombre TEXT,  DNI TEXT, Direccion TEXT, Nacimiento TEXT, Telefono TEXT, Correo TEXT, Cuenta TEXT)")
    cur.execute("CREATE TABLE Proveedores (Id INTEGER PRIMARY KEY, Codigo TEXT, Descripcion TEXT, Direccion TEXT, Telefono TEXT, Correo TEXT)")
except:
    pass

con.close()

