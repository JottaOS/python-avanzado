import datetime

import flet as ft

FORMATO_FECHA = "%d/%m/%Y"


def fecha_local(valor):
    if isinstance(valor, datetime.datetime) and valor.tzinfo is not None:
        return valor.astimezone().date()
    if isinstance(valor, datetime.datetime):
        return valor.date()
    return valor


def fecha_hoy() -> datetime.date:
    return fecha_local(datetime.datetime.now().astimezone())


def abrir_date_picker(page: ft.Page, campos: dict[str, ft.Control]):
    hoy = fecha_hoy()
    picker = ft.DatePicker(
        value=datetime.datetime.now().astimezone(),
        first_date=datetime.date(hoy.year - 10, 1, 1),
        last_date=datetime.date(hoy.year + 10, 12, 31),
        on_change=lambda e: cambiar_fecha(e, page, campos),
    )
    page.show_dialog(picker)


def cambiar_fecha(e, page: ft.Page, campos: dict[str, ft.Control]):
    if e.control.value is not None:
        fecha_ingreso = campos["fecha_ingreso"]
        fecha_ingreso.value = fecha_local(e.control.value).strftime(FORMATO_FECHA)
        fecha_ingreso.error_text = None
        page.update()


def validar(campos: dict[str, ft.Control]) -> list[str]:
    marca = campos["marca"]
    modelo = campos["modelo"]
    anio = campos["anio"]
    tipo_vehiculo = campos["tipo_vehiculo"]
    precio = campos["precio"]
    fecha_ingreso = campos["fecha_ingreso"]

    errores: list[str] = []

    marca.error_text = None
    modelo.error_text = None
    anio.error_text = None
    precio.error_text = None
    fecha_ingreso.error_text = None

    if not marca.value:
        marca.error_text = "La marca no puede estar vacía."
        errores.append("Marca no puede estar vacía.")

    if not modelo.value:
        modelo.error_text = "El modelo no puede estar vacío."
        errores.append("Modelo no puede estar vacío.")

    try:
        anio_num = int(anio.value)
        if anio_num <= 1900:
            raise ValueError
    except (ValueError, TypeError):
        anio.error_text = "Debe ser un año numérico mayor a 1900."
        errores.append("Año debe ser numérico y mayor a 1900.")

    if not tipo_vehiculo.value:
        errores.append("Tipo de vehículo debe estar seleccionado.")

    try:
        if precio.value:
            float(precio.value)
    except ValueError:
        precio.error_text = "Debe ser numérico."
        errores.append("Precio debe ser numérico.")

    try:
        dia, mes, anio_dt = map(int, fecha_ingreso.value.split("/"))
        datetime.date(anio_dt, mes, dia)
    except (ValueError, TypeError):
        fecha_ingreso.error_text = "Debe ser una fecha válida (dd/mm/aaaa)."
        errores.append("Fecha de ingreso debe ser válida.")

    return errores


def cerrar_dialogo(page: ft.Page):
    page.pop_dialog()


def guardar(page: ft.Page, campos: dict[str, ft.Control]):
    errores = validar(campos)
    if errores:
        mensaje = "\n".join(f"- {err}" for err in errores)
        dlg = ft.AlertDialog(
            title=ft.Text("Errores de validación"),
            content=ft.Text(mensaje),
            actions=[ft.TextButton("OK", on_click=lambda e: cerrar_dialogo(page))],
            modal=True,
        )
        page.show_dialog(dlg)
        page.update()
        return

    dlg = ft.AlertDialog(
        title=ft.Text("Datos del vehículo"),
        content=ft.Text(
            "DATOS DEL VEHÍCULO\n"
            f"Marca: {campos['marca'].value}\n"
            f"Modelo: {campos['modelo'].value}\n"
            f"Chasis: {campos['chasis'].value}\n"
            f"Año: {campos['anio'].value}\n"
            f"Tipo: {campos['tipo_vehiculo'].value}\n\n"
            "DATOS TÉCNICOS\n"
            f"Color: {campos['color'].value}\n"
            f"Kilometraje: {campos['kilometraje'].value}\n"
            f"Combustible: {campos['combustible'].value}\n\n"
            "DATOS ADMINISTRATIVOS\n"
            f"Precio: {campos['precio'].value}\n"
            f"Fecha de ingreso: {campos['fecha_ingreso'].value}"
        ),
        actions=[ft.TextButton("OK", on_click=lambda e: cerrar_dialogo(page))],
        modal=True,
    )
    page.show_dialog(dlg)


def limpiar(page: ft.Page, campos: dict[str, ft.Control]):
    for nombre in ("marca", "tipo_vehiculo", "combustible"):
        campos[nombre].value = None
    for nombre in ("modelo", "chasis", "anio", "color", "kilometraje", "precio"):
        campos[nombre].value = ""
    campos["fecha_ingreso"].value = fecha_hoy().strftime(FORMATO_FECHA)

    for nombre in ("marca", "modelo", "anio", "precio", "fecha_ingreso"):
        campos[nombre].error_text = None
    page.update()


def main(page: ft.Page):
    page.title = "Registro de Vehículos"
    page.padding = 20
    page.scroll = ft.ScrollMode.ADAPTIVE

    marca = ft.Dropdown(
        label="Marca",
        options=[
            ft.DropdownOption(key="Toyota", text="Toyota"),
            ft.DropdownOption(key="Ford", text="Ford"),
            ft.DropdownOption(key="Chevrolet", text="Chevrolet"),
            ft.DropdownOption(key="Volkswagen", text="Volkswagen"),
            ft.DropdownOption(key="Honda", text="Honda"),
            ft.DropdownOption(key="Nissan", text="Nissan"),
        ],
        col={"xs": 12, "md": 6},
    )
    modelo = ft.TextField(label="Modelo", col={"xs": 12, "md": 6})
    chasis = ft.TextField(label="Número de Chasis", col={"xs": 12, "md": 6})
    anio = ft.TextField(
        label="Año",
        keyboard_type=ft.KeyboardType.NUMBER,
        col={"xs": 12, "md": 6},
    )
    tipo_vehiculo = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="Auto", label="Auto"),
                ft.Radio(value="Camioneta", label="Camioneta"),
                ft.Radio(value="Camión", label="Camión"),
            ]
        ),
        col={"xs": 12, "md": 6},
    )

    color = ft.TextField(label="Color", col={"xs": 12, "md": 6})
    kilometraje = ft.TextField(
        label="Kilometraje",
        keyboard_type=ft.KeyboardType.NUMBER,
        col={"xs": 12, "md": 6},
    )
    combustible = ft.Dropdown(
        label="Combustible",
        options=[
            ft.DropdownOption(key="Nafta", text="Nafta"),
            ft.DropdownOption(key="Diésel", text="Diésel"),
            ft.DropdownOption(key="Eléctrico", text="Eléctrico"),
            ft.DropdownOption(key="Híbrido", text="Híbrido"),
        ],
        col={"xs": 12, "md": 6},
    )

    precio = ft.TextField(
        label="Precio",
        keyboard_type=ft.KeyboardType.NUMBER,
        col={"xs": 12, "md": 6},
    )
    fecha_ingreso = ft.TextField(
        label="Fecha de ingreso",
        value=fecha_hoy().strftime(FORMATO_FECHA),
        read_only=True,
        col={"xs": 12, "md": 6},
    )

    campos: dict[str, ft.Control] = {
        "marca": marca,
        "modelo": modelo,
        "chasis": chasis,
        "anio": anio,
        "tipo_vehiculo": tipo_vehiculo,
        "color": color,
        "kilometraje": kilometraje,
        "combustible": combustible,
        "precio": precio,
        "fecha_ingreso": fecha_ingreso,
    }

    botones = ft.Row(
        controls=[
            ft.Button(
                "Guardar",
                icon=ft.Icons.SAVE,
                on_click=lambda e: guardar(page, campos),
            ),
            ft.Button(
                "Limpiar",
                icon=ft.Icons.CLEAR,
                on_click=lambda e: limpiar(page, campos),
            ),
        ],
        spacing=20,
    )

    controles: list[ft.Control] = [
        ft.Text("Registro de Vehículos", size=24, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        ft.Text("1) Datos del vehículo", size=20, weight=ft.FontWeight.BOLD),
        ft.ResponsiveRow([marca, modelo, chasis, anio, tipo_vehiculo]),
        ft.Text("2) Datos técnicos", size=20, weight=ft.FontWeight.BOLD),
        ft.ResponsiveRow([color, kilometraje, combustible]),
        ft.Text("3) Datos administrativos", size=20, weight=ft.FontWeight.BOLD),
        ft.ResponsiveRow(
            [
                precio,
                ft.Row(
                    controls=[
                        fecha_ingreso,
                        ft.IconButton(
                            icon=ft.Icons.CALENDAR_MONTH,
                            tooltip="Seleccionar fecha",
                            on_click=lambda e: abrir_date_picker(page, campos),
                        ),
                    ],
                    col={"xs": 12, "md": 6},
                ),
            ]
        ),
        botones,
    ]

    page.add(ft.Column(controls=controles, spacing=25))


ft.run(main)
