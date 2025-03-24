from database.mongodb.init_mongodb_db import get_mongodb_client
from bson import ObjectId

db = get_mongodb_client()

references_collection = db['references']

references = [
    {
    "title": "The Best Workout Splits For Every Goal",
    "author": "Alex Kirkup-Lee",
    "publication_date": "2024-05-20",
    "url": "https://uk.gymshark.com/blog/article/the-best-workout-splits-for-every-goal",
    "vector_db": "workout_split_db",
    "references": [
        {
            "author": "Schoenfeld, B.J., Grgic, J. and Krieger, J.",
            "year": 2018,
            "title": "How many times per week should a muscle be trained to maximize muscle hypertrophy? A systematic review and meta-analysis of studies examining the effects of resistance training frequency."
        },
        {
            "author": "Aston University",
            "year": "n.d.",
            "title": "The Push/Pull/Legs Routine for Muscle Gains | Aston University."
        },
        {
            "author": "Schoenfeld, B.J., Ogborn, D. and Krieger, J.W.",
            "year": 2017,
            "title": "Dose-response relationship between weekly resistance training volume and increases in muscle mass: A systematic review and meta-analysis."
        },
        {
            "author": "Schoenfeld, B.J., Ogborn, D. and Krieger, J.W.",
            "year": 2016,
            "title": "Effects of Resistance Training Frequency on Measures of Muscle Hypertrophy: A Systematic Review and Meta-Analysis."
        },
        {
            "author": "Ribeiro, A.S., Schoenfeld, B.J., Silva, D.R.P., Pina, F.L.C., Guariglia, D.A., Porto, M., Maestá, N., Burini, R.C. and Cyrino, E.S.",
            "year": 2015,
            "title": "Effect of Two- Versus Three-Way Split Resistance Training Routines on Body Composition and Muscular Strength in Bodybuilders: A Pilot Study."
        },
        {
            "author": "Roberts, B.M., Nuckols, G. and Krieger, J.W.",
            "year": 2020,
            "title": "Sex Differences in Resistance Training."
        },
        {
            "author": "Cureton, K.J., Collins, M.A., Hill, D.W. and McElhannon, F.M.",
            "year": 1988,
            "title": "Muscle hypertrophy in men and women."
        }
    ]
},
{
    "title": "The BEST Workout Split to Build Muscle (in 2025)",
    "author": "Jeremy Ethier",
    "publication_date": "2024-11-24",
    "url": "https://builtwithscience.com/fitness-tips/best-workout-split-2025/",
    "references": [
        {
            "author": "Pelland, J., Remmert, J., Robinson, Z., Hinson, S., Zourdos, M.",
            "year": 2024,
            "title": "The resistance training dose-response: Meta-regressions exploring the effects of weekly volume and frequency on muscle hypertrophy and strength gain.",
            "url": "http://dx.doi.org/10.51224/srxiv.460"
        },
        {
            "author": "Damas, F., Phillips, S., Vechin, F. C., Ugrinowitsch, C.",
            "year": 2015,
            "title": "A review of resistance training-induced changes in skeletal muscle protein synthesis and their contribution to hypertrophy.",
            "journal": "Sports medicine (Auckland, N.Z.)",
            "volume": "45(6)",
            "pages": "801–807"
        },
        {
            "author": "Zaroni, R. S., Brigatto, F. A., Schoenfeld, B. J., Braz, T. V., Benvenutti, J. C., Germano, M. D., Marchetti, P. H., Aoki, M. S., Lopes, C. R.",
            "year": 2019,
            "title": "High resistance-training frequency enhances muscle thickness in resistance-trained men.",
            "journal": "Journal of strength and conditioning research",
            "volume": "33 Suppl 1",
            "pages": "S140–S151"
        }
    ]
}

]

def references_init():
  
  state = False

  result = references_collection.insert_many(references)

  if len(result.inserted_ids) == len(references):
   state = True
    
  return state


