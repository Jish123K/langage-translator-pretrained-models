import argparse

import fairseq

import sys

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--source", type=str, required=True, help="The source code to translate.")

    parser.add_argument("--target", type=str, required=True, help="The target language.")

    parser.add_argument("--model", type=str, required=True, help="The path to the fairseq model.")

    parser.add_argument("--beam", type=int, default=5, help="The beam size for beam search.")

    parser.add_argument("--nbest", type=int, default=1, help="The number of best hypotheses to output.")

    args = parser.parse_args()

    # Load the fairseq model.

    model = fairseq.models.bart.BartModel.from_pretrained(args.model)

    # Translate the source code.

    translations = model.translate(

        args.source,

        beam=args.beam,

        nbest=args.nbest,

        target_lang=args.target,

    )

    # Print the translations.

    for translation in translations:

        print(translation)

if __name__ == "__main__":

    main()
