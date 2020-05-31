# Data Generation

Conjunto de arquivos que permitem gerar ODFs e PeDFs através de um sinal temporal.

## Arquivos

 - DataGeneration.ipynb: Execução com comentários de como importar um arquivo de áudio e gerar ODFs e PeDFs
 - gpad_data_generation.py: modulo com todas as funções necessarias para carregar um arquivo de áudio e gerar suas ODFs e PeDFs

## Functions in gpad_data_generation.py

### convert_mp3_to_wav(filename)
converts a mp3 file to a wav file
    
    Arguments:
    filename -- string with the name of the mp3 file
                e.g.: filename = "/Music/saudade.mp3"
    
    Returns: 
    /~/filename.wav


### music_loading(filename, sample_rate=44100)
   loads one music to the memory as a normalized numpy array
    
    Arguments:
    filename    -- string with the name of the mp3 file
                   e.g.: filename = "/Music/saudade.mp3"
    sample_rate -- [OPTIONAL] sample rate of the music in Hertz
    
    Returns: 
    musica      -- a numpy array of dimensions (n,1) with n the number of samples of the music

### ODF_SuperFlux(signal, sample_rate, frame_size, hop)
computes the Onset Detection Function of a signal
    
    Arguments:
    signal      -- a numpy array of dimensions (n,1)
    sample_rate -- sample rate of the signal in Hertz
    frame_size  -- size in samples of the frames that will build the spectogram
    hop         -- distance in samples between the frame i+1 and the frame i
    
    Returns: 
    ODF         -- a numpy array of dimension (n,1) with n the number of samples of the ODF

### PeDF(ODF, form)
computes the Periodicity Function, a normalized autocorrelation of the ODF signal
    
    Arguments:
    ODF         -- a numpy array of dimensions (n,1)
    form        -- definition of PeDF calculation
                    'full'    -> The output will be a symetric signal, the full autocorrelation
                    'partial' -> The output will be one half of the full autocorrelation
    
    Returns: 
    PeDF        -- a numpy array of dimension (n,1) with n the number of samples of the PeDF

### preprocess(signal_we_want_to_analyze, nivel_wavelet)
realizes the preprocessing of a signal to output its ODFs, PeDFs and wavelet coefficients
    
    Arguments:
    signal_we_want_to_analyze  -- a numpy array of dimensions (n,1)
    nivel_wavelet              -- the level of the wavelet transform
    
    Returns: 
    ODF_SET                    -- a list containing ODFs functions
    PeDF_FULL_SET              -- a list containing the whole PeDFs functions
    PeDF_PARTIAL_SET           -- a list containing the halfs of the PeDFs functions
    coeffs                     -- the wavelet coefficients of the wavelet transform decomposition over "signal_we_want_to_analyze"

### music_processor(filename, start_sample=524288, final_sample=1048576, sample_rate=44100, nivel_wavelet=5)
realizes the preprocessing of a music file's segment to output its ODFs, PeDFs and wavelet coefficients
    
    Arguments:
    filename                   -- string with the name of the mp3 file
                                  e.g.: filename = "/Music/saudade.mp3"
    start_sample               -- [OPTIONAL] starting sample of the audio segment exctracted of "file"
    final_sample               -- [OPTIONAL] final sample of the audio segment exctracted of "file"
    sample_rate                -- [OPTIONAL] the sample rate of "file"
    nivel_wavelet              -- [OPTIONAL] the level of the wavelet transform decomposition
    
    Returns: 
    ODF_SET                    -- a list containing ODFs functions
    PeDF_FULL_SET              -- a list containing the whole PeDFs functions
    PeDF_PARTIAL_SET           -- a list containing the halfs of the PeDFs functions
    coeffs                     -- the wavelet coefficients of the wavelet transform over "signal_we_want_to_analyze"

### plot_ODF(ODF, index=None, size=None)
realizes the plotting of the ODF
    
    Arguments:
    ODF        -- a numpy array of dimensions (n,1)
    index      -- the ODF level corresponding to its wavelet coefficients
    size       -- the level of the wavelet decomposition that generated all the ODFs
    
    Returns: 
    the plot of the ODF in (samples,Onset Stregth)

### plot_PeDF(PeDF, form, index=None, size=None)
realizes the plotting of the PeDF
    
    Arguments:
    ODF        -- a numpy array of dimensions (n,1)
    form       -- 'total' or 'partial', related to the PeDF's aspect
    index      -- the PeDF level corresponding to its wavelet coefficients
    size       -- the level of the wavelet decomposition that generated all the PeDFs
    
    Returns: 
    the plot of the PeDF in (lags,autocorrelation probability)

## Documentações Auxiliares
 - https://madmom.readthedocs.io/en/latest/modules/audio/signal.html
 - https://madmom.readthedocs.io/en/latest/modules/audio/spectrogram.html
 - https://madmom.readthedocs.io/en/latest/modules/features/onsets.html

## Referências Bibliográficas

FERNANDES JUNIOR, Antonio Carlos Lopes. Contribuições ao problema de extração de tempo musical. 2015. 122 p. Tese (doutorado) - Universidade Estadual de Campinas, Faculdade de Engenharia Elétrica e de Computação, Campinas, SP

SINEZIO, H. M.; FERNANDES JR., A. C. L. . Atributos Extraídos de Funções de Detecção de Periodicidade para Extração de Andamento Musical. In: VIII Conferência Nacional em Comunicação, Redes e Segurança da Informação, 2018, Salvador. Anais do ENCOM, 2018. p. 147-148.

Sebastian Böck and Gerhard Widmer, “Maximum Filter Vibrato Suppression for Onset Detection”, Proceedings of the 16th International Conference on Digital Audio Effects (DAFx), 2013.

S. Bock, F. Korzeniowski, J. Schluter, F. Krebs, and G. Widmer,  “madmom:  a new python audio and music signal processing library,”  in Proceedings of the 24th ACM International Conference on Multimedia, 2016, ACMMM.
