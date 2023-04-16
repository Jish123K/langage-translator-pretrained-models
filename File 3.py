import torch

import onmt

import onmt.inputters

import onmt.translate

import onmt.model_builder

import onmt.opts

# load the pre-trained model

model_path = "path/to/model.pt"

fields_path = "path/to/fields.pt"

model_opts_path = "path/to/model_opts.yaml"

fields = torch.load(fields_path)

model_opts = onmt.opts.ModelOpts.from_yaml_file(model_opts_path)

model = onmt.model_builder.build_base_model(

    model_opts, fields, use_gpu=False, gpu_id=None)

model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))

# create the translator

translator = onmt.translate.Translator(

    model=model,

    fields=fields,

    beam_size=5,

    n_best=1,

    max_length=50,

    global_scores=None,

    copy_attn=model_opts.copy_attn,

    cuda=False,

    beam_trace=False,

    min_length=0,

    stepwise_penalty=False,

    block_ngram_repeat=0,

    ignore_when_blocking=[],

    replace_unk=False,

    phrase_table="",

    verbose=False,

    report_time=False,

    attn_debug=False,

    dump_beam="",

    num_workers=0)

# translate some text

src_text = "Hello, how are you?"

src_data = {'src': [src_text]}

dataset = onmt.inputters.Dataset(

    src_data, fields, None, None,

    None, None,

    None, None)

data_iter = onmt.inputters.OrderedIterator(

    dataset=dataset,

    device=torch.device('cpu'),

    batch_size=1,

    train=False,

    sort=False,

    sort_within_batch=True,

    shuffle=False)

for batch in data_iter:

    trans_batch = translator.translate_batch(batch, data_iter.src_vocabs)

    translations = translator.from_batch(trans_batch)

    for translation in translations:

        print(translation.pred_sents[0])

