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
    "vector_db": "training_availability_db",
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
    "vector_db": "training_availability_db",
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
},
{
    "title": "The Best Dumbbell Exercises To Target Every Muscle",
    "author": "Alex Kirkup-Lee",
    "publication_date": "2025-03-21",
    "url": "https://uk.gymshark.com/blog/article/the-best-dumbbell-exercises",
    "vector_db": "available_equipment_db",
    "references": [
        {
            "author": "Smoak, Y.",
            "year": 2023,
            "title": "A Randomised Trial Comparing Barbell and Dumbbell Bench Press on Maximal Strength and Power Output."
        },
        {
            "author": "Saeterbakken, A.H., van den Tillaar, R. and Fimland, M.S.",
            "year": 2011,
            "title": "A comparison of muscle activity and 1-RM strength of three chest-press exercises with different stability requirements."
        },
        {
            "author": "Schoenfeld, B.J. and Grgic, J.",
            "year": 2020,
            "title": "Effects of range of motion on muscle development during resistance training interventions: A systematic review."
        },
        {
            "author": "Schoenfeld, B.J., Vigotsky, A., Contreras, B., Golden, S., Alto, A., Larson, R., Winkelman, N. and Paoli, A.",
            "year": 2018,
            "title": "Differential effects of attentional focus strategies during long-term resistance training."
        },
        {
            "author": "Maeo, S., Wu, Y., Huang, M., Sakurai, H., Kusagawa, Y., Sugiyama, T., Kanehisa, H. and Isaka, T.",
            "year": 2022,
            "title": "Triceps brachii hypertrophy is substantially greater after elbow extension training performed in the overhead versus neutral arm position."
        },
        {
            "author": "Solstad, T.E., Andersen, V., Shaw, M., Hoel, E.M., Vonheim, A. and Atle Hole Saeterbakken.",
            "year": 2020,
            "title": "A Comparison of Muscle Activation between Barbell Bench Press and Dumbbell Flyes in Resistance-Trained Males."
        },
        {
            "author": "Schoenfeld, B.J., Peterson, M.D., Ogborn, D., Contreras, B. and Sonmez, G.T.",
            "year": 2015,
            "title": "Effects of Low- vs. High-Load Resistance Training on Muscle Strength and Hypertrophy in Well-Trained Men."
        }
    ]
},
{
    "title": "Your Next Chest Routine for Mass: 7 Must-Do Pec Exercises",
    "author": "Michael Matthews",
    "publication_date": "2024-09-13",
    "url": "https://legionathletics.com/chest-workouts/",
    "vector_db": "available_equipment_db",
    "references": [
        {
            "author": "Wolf, Milo, et al.",
            "year": 2022,
            "title": "Partial vs Full Range of Motion Resistance Training: A Systematic Review and Meta-Analysis."
        },
        {
            "author": "Martínez-Cava, Alejandro, et al.",
            "year": 2019,
            "title": "Bench Press at Full Range of Motion Produces Greater Neuromuscular Adaptations than Partial Executions after Prolonged Resistance Training."
        },
        {
            "author": "Costa, Bruna Daniella de Vasconcelos, et al.",
            "year": 2021,
            "title": "Does Performing Different Resistance Exercises for the Same Muscle Group Induce Non-Homogeneous Hypertrophy?"
        },
        {
            "author": "Kristiansen, M., et al.",
            "year": 2013,
            "title": "Inter-Subject Variability of Muscle Synergies during Bench Press in Power Lifters and Untrained Individuals."
        },
        {
            "author": "Oranchuk, Dustin J., et al.",
            "year": 2019,
            "title": "Isometric Training and Long-Term Adaptations: Effects of Muscle Length, Intensity, and Intent: A Systematic Review."
        },
        {
            "author": "Liao, Kai-Fang, et al.",
            "year": 2021,
            "title": "Effects of Unilateral vs. Bilateral Resistance Training Interventions on Measures of Strength, Jump, Linear and Change of Direction Speed: A Systematic Review and Meta-Analysis."
        },
        {
            "author": "Barnett, Chris, et al.",
            "year": 1995,
            "title": "Effects of Variations of the Bench Press Exercise on the EMG Activity of Five Shoulder Muscles."
        },
        {
            "author": "Afonso, José, et al.",
            "year": 2021,
            "title": "Strength Training versus Stretching for Improving Range of Motion: A Systematic Review and Meta-Analysis."
        }
    ]
},
{
    "title": "The Best Back Workout Routine for Mass & Hypertrophy",
    "author": "Michael Matthews",
    "publication_date": "2024-06-28",
    "url": "https://legionathletics.com/back-workouts/",
    "vector_db": "available_equipment_db",
    "references": [
        {
            "author": "Nigro, Federico, and Sandro Bartolomei",
            "year": 2020,
            "title": "A Comparison between the Squat and the Deadlift for Lower Body Strength and Power Training."
        },
        {
            "author": "Youdas, James W, et al.",
            "year": 2010,
            "title": "Surface Electromyographic Activation Patterns and Elbow Joint Motion during a Pull-Up, Chin-Up, or Perfect-Pullup™ Rotational Exercise."
        },
        {
            "author": "Dickie, James A., et al.",
            "year": 2016,
            "title": "Electromyographic Analysis of Muscle Activation during Pull-up Variations."
        },
        {
            "author": "Liao, Kai-Fang, et al.",
            "year": 2022,
            "title": "Review Paper Effects of Unilateral vs. Bilateral Resistance Training Interventions on Measures of Strength, Jump, Linear and Change of Direction Speed: A Systematic Review and Meta-Analysis."
        },
        {
            "author": "Park, Se-yeon, and Won-gyu Yoo",
            "year": 2014,
            "title": "Differential Activation of Parts of the Latissimus Dorsi with Various Isometric Shoulder Exercises."
        },
        {
            "author": "Gerling, Michael E., and Stephen H. M. Brown",
            "year": 2013,
            "title": "Architectural Analysis and Predicted Functional Capability of the Human Latissimus Dorsi Muscle."
        },
        {
            "author": "Schoenfeld, Brad J, and Jozo Grgic",
            "year": 2020,
            "title": "Effects of Range of Motion on Muscle Development during Resistance Training Interventions: A Systematic Review."
        },
        {
            "author": "Oranchuk, Dustin J., et al.",
            "year": 2019,
            "title": "Isometric Training and Long-Term Adaptations: Effects of Muscle Length, Intensity, and Intent: A Systematic Review."
        }
    ]
},
{
    "title": "The Best Full Shoulder Exercises for Building Size and Mass",
    "author": "Michael Matthews",
    "publication_date": "2024-05-17",
    "url": "https://legionathletics.com/shoulder-workouts/",
    "vector_db": "available_equipment_db",
    "references": [
        {
            "author": "Saeterbakken, Atle H., and Marius S. Fimland",
            "year": 2013,
            "title": "Effects of Body Position and Loading Modality on Muscle Activity and Strength in Shoulder Presses."
        },
        {
            "author": "Raizada, Shiny, and Amritashish Bagchi",
            "year": 2017,
            "title": "Comparison among the EMG Activity of the Anterior Deltoid and Medial Deltoid during Two Variations of Dumbbell Shoulder Press Exercise."
        },
        {
            "author": "Schoenfeld, Brad J, et al.",
            "year": 2011,
            "title": "The Upright Row: Implications for Preventing Subacromial Impingement."
        },
        {
            "author": "Page, Phil",
            "year": 2011,
            "title": "Shoulder Muscle Imbalance and Subacromial Impingement Syndrome in Overhead Athletes."
        },
        {
            "author": "Franke, Rodrigo, et al.",
            "year": 2014,
            "title": "Analysis of Anterior, Middle and Posterior Deltoid Activation during Single and Multijoint Exercises."
        }
    ]
},
{
    "title": "Leg Day Workout Routine for Hypertrophy & Building Mass",
    "author": "Michael Matthews",
    "publication_date": "2024-03-19",
    "url": "https://legionathletics.com/leg-workouts/",
    "vector_db": "available_equipment_db",
    "references": [
        {
            "author": "Yavuz, Hasan Ulas, et al.",
            "year": 2015,
            "title": "Kinematic and EMG Activities during Front and Back Squat Variations in Maximum Loads."
        },
        {
            "author": "Gullett, Jonathan C, et al.",
            "year": 2009,
            "title": "A Biomechanical Comparison of Back and Front Squats in Healthy Trained Individuals."
        },
        {
            "author": "Jones, Margaret T, et al.",
            "year": 2012,
            "title": "Effects of Unilateral and Bilateral Lower-Body Heavy Resistance Exercise on Muscle Activity and Testosterone Responses."
        },
        {
            "author": "DeFOREST, Bradley A., et al.",
            "year": 2014,
            "title": "Muscle Activity in Single- vs. Double-Leg Squats."
        },
        {
            "author": "Wojtys, E M, et al.",
            "year": 1996,
            "title": "Neuromuscular Adaptations in Isokinetic, Isotonic, and Agility Training Programs."
        },
        {
            "author": "Gentil, Paulo, et al.",
            "year": 2015,
            "title": "Single vs. Multi-Joint Resistance Exercises: Effects on Muscle Strength and Hypertrophy."
        },
        {
            "author": "Schoenfeld, Brad J.",
            "year": 2010,
            "title": "The Mechanisms of Muscle Hypertrophy and Their Application to Resistance Training."
        },
        {
            "author": "Gonzalez, Adam M., et al.",
            "year": 2015,
            "title": "Intramuscular Anabolic Signaling and Endocrine Response Following Resistance Exercise: Implications for Muscle Hypertrophy."
        }
    ]
},
{
    "title": "How to Get a Six Pack: Tips & Exercises",
    "author": "Michael Matthews",
    "publication_date": "2024-05-14",
    "url": "https://legionathletics.com/how-to-get-six-pack-abs/",
    "vector_db": "available_equipment_db",
    "references": [
        {
            "author": "Vispute, Sachin S, et al.",
            "year": 2011,
            "title": "The Effect of Abdominal Exercise on Abdominal Fat."
        },
        {
            "author": "Stallknecht, Bente, et al.",
            "year": 2007,
            "title": "Are Blood Flow and Lipolysis in Subcutaneous Adipose Tissue Influenced by Contractions in Adjacent Muscles in Humans?"
        },
        {
            "author": "Nuzzo, James L, et al.",
            "year": 2008,
            "title": "Trunk Muscle Activity during Stability Ball and Free Weight Exercises."
        },
        {
            "author": "Moraes, Antonio C., et al.",
            "year": 2009,
            "title": "EMG Activation of Abdominal Muscles in the Crunch Exercise Performed with Different External Loads."
        },
        {
            "author": "SuppVersity EMG Series",
            "year": 2011,
            "title": "Rectus Abdominis, Obliques and Erector Spinae: The Very Best Exercises for Sixpack Abs and a Powerful Midsection."
        },
        {
            "author": "Francis, P. and Davis, J.",
            "year": 2001,
            "title": "New study puts the crunch on ineffective ab exercises."
        },
        {
            "author": "Youdas, James W, et al.",
            "year": 2008,
            "title": "An Electromyographic Analysis of the Ab-Slide Exercise, Abdominal Crunch, Supine Double Leg Thrust, and Side Bridge in Healthy Young Adults: Implications for Rehabilitation Professionals."
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


