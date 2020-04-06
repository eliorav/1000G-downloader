<p align="center">
  <h3 align="center">1000G Downloader</h3>

  <p align="center">
    Download sample from 1000G project.
  </p>
</p>

## Getting Started
### Installation

```sh
pip install one_thousand_genomes_downloader
```

### Usage example

```py
downloader = OneThousandGenomesDownloader()
downloader('HG00102')
```

## Documentation
### Class OneThousandGenomesDownloader
> OneThousandGenomesDownloader()

* file_format: the file format of the sample: bam or cram
* use_mapped_file: if to download the mapped or the unmapped file
* use_exome_alignment: if to download from the exome alignment folder
* on_download_finish: a callback function
* output_folder: output folder
## Contact
Elior Avraham – elior.av@gmail.com

