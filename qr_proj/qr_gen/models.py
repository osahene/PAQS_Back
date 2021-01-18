from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
# import itertools
import idstring
import random
from qr_reg.models import InstitutionInfo, Product, CompanyLogo

class ProdQRGen(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    # qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    qty = models.PositiveSmallIntegerField(default=1)
    product_batch = idstring.IDstring(seed='1Y3R9C')
    logo = Image.open('.\images\img2.png', "r")

    def __str__(self):
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        for i in zip(self.product_batch):
            while self.product_batch.startswith('1'):                
                self.product_batch += 1
        qr=qrcode.QRCode(
            version=12,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=5,
            border=1
            )
        qr.add_data([self.name, str(i)], optimize=20)
        qr.make(fit=True)
        qrcode_img = qr.make_image(fill_color='blue', back_color='white').convert('RGB')
        # canvas = Image.new('RGB', (290,290), 'white')
        # draw = ImageDraw.Draw(canvas)
        basewidth = 75
        wpercent = (basewidth/float(self.logo.size[0]))
        hsize = int((float(self.logo.size[1])*float(wpercent)))
        logo = self.logo.resize((basewidth,hsize), Image.ANTIALIAS)
        pos = ((qrcode_img.size[0] - logo.size[0]) // 2, (qrcode_img.size[1] - logo.size[1]) // 2)
        qrcode_img.paste(logo, pos)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        qrcode_img.save(buffer, 'PNG')
        qrcode_img.save(fname, File(buffer), save=False)
        qrcode_img.close()
        super().save(*args, **kwargs)*self.qty



        # qrcode_img.save('C:\\Users\\Teezil\\workspace\\qr_stuff.png'*self.qty)
        # canvas.paste(qrcode_img)

         

        