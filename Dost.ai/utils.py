import whisper
from neon_tts_plugin_coqui import CoquiTTS
import tempfile

model = whisper.load_model("small")

LANGUAGES = list(CoquiTTS.langs.keys())
coquiTTS = CoquiTTS()

def recognize(audio):
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    
    _, probs = model.detect_language(mel)
    lang = max(probs, key=probs.get)

    options = whisper.DecodingOptions(fp16 = False)
    result = whisper.decode(model, mel, options)
    return result

def voiceResponse(text, language):
    coqui_langs = ['en' ,'es' ,'fr' ,'de' ,'pl' ,'uk' ,'ro' ,'hu' ,'bg' ,'nl' ,'fi' ,'sl' ,'lv' ,'ga']
    if language not in coqui_langs:
      language = 'en'
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as voice:
        coquiTTS.get_tts(text, voice, speaker = {"language" : language})
    return voice