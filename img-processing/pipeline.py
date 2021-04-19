from pathlib import Path
from glob import glob

from ploomber import DAG
from ploomber.tasks import PythonCallable
from ploomber.products import File
from ploomber.executors import Parallel
from PIL import Image


def process_image(product, path_to_image):
    # define all transformations in a single function
    with Image.open(path_to_image) as img:
        rotated = img.rotate(45)
        gray = rotated.convert('L')
        gray.save(str(product))


def make():
    dag = DAG()
    Path('output').mkdir(exist_ok=True)

    # iterate over all images
    for path in glob('imagenette2-160/train/**/*.JPEG', recursive=True)[:100]:
        name = Path(path).name
        # and create one task per image
        PythonCallable(process_image,
                       File(f'output/{name}'),
                       dag=dag,
                       name=name,
                       params=dict(path_to_image=path))

    return dag
