class Tool:
    """
    Çizim uygulamasında kullanılan araçları temsil eder.
    Örneğin: Kalem (pen), fırça (brush), silgi (eraser) vb.

    Özellikler:
    - name  : Araç ismi (örn. "Kalem", "Fırça")
    - color : Renk (örn. "#000000" → siyah)
    - size  : Kalınlık (örn. 5 → 5px çizim)
    """

    def __init__(self, name: str, color: str = "#000000", size: int = 5):
        """
        Tool nesnesi oluşturur.

        :param name: Araç ismi (string)
        :param color: Renk (hex string)
        :param size: Kalınlık (int)
        """
        self.name = name
        self.color = color
        self.size = size

    def __str__(self):
        """
        Tool nesnesi yazdırıldığında ne görünecek?
        """
        return f"{self.name} (Color: {self.color}, Size: {self.size}px)"

    def set_color(self, new_color: str):
        """Aracın rengini değiştirir."""
        self.color = new_color

    def set_size(self, new_size: int):
        """Aracın kalınlığını değiştirir."""
        self.size = new_size
