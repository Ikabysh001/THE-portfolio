from pydub import AudioSegment

def convert_ogg2wav(ofn):

    wfn = ofn.replace('.ogg','.wav')
    x = AudioSegment.from_file(ofn)
    x.export(wfn, format='wav')


convert_ogg2wav("voice_note.ogg")    

