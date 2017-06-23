from distutils.core import setup


long_description = """
Make your google cast device seems like a normal DLNA renderer.
"""
version = '0.1.0'


def main():
    setup(
        name='castproxy',
        version=version,
        description='Cast proxy for google cast',
        long_description=long_description,
        author='zhaohui',
        author_email='zhaohui-sol@foxmail.com',
        url='https://isol.me',
        download_url='https://isol.me',
        license='GPL',
        platforms='any',
        scripts=['bin/castproxy'],
        keywords=['UPnP', 'Google Cats', 'DLNA', 'Rendering'],
        package_dir={
            'castproxy': 'castproxy'
        },
        packages=[
            'castproxy'
        ],
        package_data={},
        data_files=[]
    )

if __name__ == "__main__":
    main()
