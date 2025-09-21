import imageio.v3 as iio

files = ['ER1.png','ER2.png','ER3.png','ER4.png','ER5.png']
images = [iio.imread(i) for i in files]
iio.imwrite('team.gif', images ,duration = 200,loop = 0)

