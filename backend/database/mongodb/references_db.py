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
    "vector_db": "workout_splits_db",
    "textfile_name": "best_workout_splits_GS.txt",
    "reviewers": [],
    "references": [
        {
            "authors": "Schoenfeld, B.J., Grgic, J. and Krieger, J.",
            "year": 2018,
            "title": "How many times per week should a muscle be trained to maximize muscle hypertrophy? A systematic review and meta-analysis of studies examining the effects of resistance training frequency."
        },
        {
            "authors": "Aston University",
            "year": "n.d.",
            "title": "The Push/Pull/Legs Routine for Muscle Gains | Aston University."
        },
        {
            "authors": "Schoenfeld, B.J., Ogborn, D. and Krieger, J.W.",
            "year": 2017,
            "title": "Dose-response relationship between weekly resistance training volume and increases in muscle mass: A systematic review and meta-analysis."
        },
        {
            "authors": "Schoenfeld, B.J., Ogborn, D. and Krieger, J.W.",
            "year": 2016,
            "title": "Effects of Resistance Training Frequency on Measures of Muscle Hypertrophy: A Systematic Review and Meta-Analysis."
        },
        {
            "authors": "Ribeiro, A.S., Schoenfeld, B.J., Silva, D.R.P., Pina, F.L.C., Guariglia, D.A., Porto, M., Maestá, N., Burini, R.C. and Cyrino, E.S.",
            "year": 2015,
            "title": "Effect of Two- Versus Three-Way Split Resistance Training Routines on Body Composition and Muscular Strength in Bodybuilders: A Pilot Study."
        },
        {
            "authors": "Roberts, B.M., Nuckols, G. and Krieger, J.W.",
            "year": 2020,
            "title": "Sex Differences in Resistance Training."
        },
        {
            "authors": "Cureton, K.J., Collins, M.A., Hill, D.W. and McElhannon, F.M.",
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
    "vector_db": "workout_splits_db",
    "textfile_name": "best_workout_splits_BWS.txt",
    "reviewers": [],
    "references": [
        {
            "authors": "Pelland, J., Remmert, J., Robinson, Z., Hinson, S., Zourdos, M.",
            "year": 2024,
            "title": "The resistance training dose-response: Meta-regressions exploring the effects of weekly volume and frequency on muscle hypertrophy and strength gain.",
            "url": "http://dx.doi.org/10.51224/srxiv.460"
        },
        {
            "authors": "Damas, F., Phillips, S., Vechin, F. C., Ugrinowitsch, C.",
            "year": 2015,
            "title": "A review of resistance training-induced changes in skeletal muscle protein synthesis and their contribution to hypertrophy.",
            "journal": "Sports medicine (Auckland, N.Z.)",
            "volume": "45(6)",
            "pages": "801–807"
        },
        {
            "authors": "Zaroni, R. S., Brigatto, F. A., Schoenfeld, B. J., Braz, T. V., Benvenutti, J. C., Germano, M. D., Marchetti, P. H., Aoki, M. S., Lopes, C. R.",
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
    "vector_db": "workout_exercises_db",
    "textfile_name": "best_dumbbell_exercises_GS.txt",
    "reviewers": [],
    "references": [
        {
            "authors": "Smoak, Y.",
            "year": 2023,
            "title": "A Randomised Trial Comparing Barbell and Dumbbell Bench Press on Maximal Strength and Power Output."
        },
        {
            "authors": "Saeterbakken, A.H., van den Tillaar, R. and Fimland, M.S.",
            "year": 2011,
            "title": "A comparison of muscle activity and 1-RM strength of three chest-press exercises with different stability requirements."
        },
        {
            "authors": "Schoenfeld, B.J. and Grgic, J.",
            "year": 2020,
            "title": "Effects of range of motion on muscle development during resistance training interventions: A systematic review."
        },
        {
            "authors": "Schoenfeld, B.J., Vigotsky, A., Contreras, B., Golden, S., Alto, A., Larson, R., Winkelman, N. and Paoli, A.",
            "year": 2018,
            "title": "Differential effects of attentional focus strategies during long-term resistance training."
        },
        {
            "authors": "Maeo, S., Wu, Y., Huang, M., Sakurai, H., Kusagawa, Y., Sugiyama, T., Kanehisa, H. and Isaka, T.",
            "year": 2022,
            "title": "Triceps brachii hypertrophy is substantially greater after elbow extension training performed in the overhead versus neutral arm position."
        },
        {
            "authors": "Solstad, T.E., Andersen, V., Shaw, M., Hoel, E.M., Vonheim, A. and Atle Hole Saeterbakken.",
            "year": 2020,
            "title": "A Comparison of Muscle Activation between Barbell Bench Press and Dumbbell Flyes in Resistance-Trained Males."
        },
        {
            "authors": "Schoenfeld, B.J., Peterson, M.D., Ogborn, D., Contreras, B. and Sonmez, G.T.",
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
    "vector_db": "workout_exercises_db",
    "textfile_name": "best_chest_exercises_Legion.txt",
    "reviewers": [],
    "references": [
        {
            "authors": "Wolf, Milo, et al.",
            "year": 2022,
            "title": "Partial vs Full Range of Motion Resistance Training: A Systematic Review and Meta-Analysis."
        },
        {
            "authors": "Martínez-Cava, Alejandro, et al.",
            "year": 2019,
            "title": "Bench Press at Full Range of Motion Produces Greater Neuromuscular Adaptations than Partial Executions after Prolonged Resistance Training."
        },
        {
            "authors": "Costa, Bruna Daniella de Vasconcelos, et al.",
            "year": 2021,
            "title": "Does Performing Different Resistance Exercises for the Same Muscle Group Induce Non-Homogeneous Hypertrophy?"
        },
        {
            "authors": "Kristiansen, M., et al.",
            "year": 2013,
            "title": "Inter-Subject Variability of Muscle Synergies during Bench Press in Power Lifters and Untrained Individuals."
        },
        {
            "authors": "Oranchuk, Dustin J., et al.",
            "year": 2019,
            "title": "Isometric Training and Long-Term Adaptations: Effects of Muscle Length, Intensity, and Intent: A Systematic Review."
        },
        {
            "authors": "Liao, Kai-Fang, et al.",
            "year": 2021,
            "title": "Effects of Unilateral vs. Bilateral Resistance Training Interventions on Measures of Strength, Jump, Linear and Change of Direction Speed: A Systematic Review and Meta-Analysis."
        },
        {
            "authors": "Barnett, Chris, et al.",
            "year": 1995,
            "title": "Effects of Variations of the Bench Press Exercise on the EMG Activity of Five Shoulder Muscles."
        },
        {
            "authors": "Afonso, José, et al.",
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
    "vector_db": "workout_exercises_db",
    "textfile_name": "best_back_exercises_Legion.txt",
    "reviewers": [],
    "references": [
        {
            "authors": "Nigro, Federico, and Sandro Bartolomei",
            "year": 2020,
            "title": "A Comparison between the Squat and the Deadlift for Lower Body Strength and Power Training."
        },
        {
            "authors": "Youdas, James W, et al.",
            "year": 2010,
            "title": "Surface Electromyographic Activation Patterns and Elbow Joint Motion during a Pull-Up, Chin-Up, or Perfect-Pullup™ Rotational Exercise."
        },
        {
            "authors": "Dickie, James A., et al.",
            "year": 2016,
            "title": "Electromyographic Analysis of Muscle Activation during Pull-up Variations."
        },
        {
            "authors": "Liao, Kai-Fang, et al.",
            "year": 2022,
            "title": "Review Paper Effects of Unilateral vs. Bilateral Resistance Training Interventions on Measures of Strength, Jump, Linear and Change of Direction Speed: A Systematic Review and Meta-Analysis."
        },
        {
            "authors": "Park, Se-yeon, and Won-gyu Yoo",
            "year": 2014,
            "title": "Differential Activation of Parts of the Latissimus Dorsi with Various Isometric Shoulder Exercises."
        },
        {
            "authors": "Gerling, Michael E., and Stephen H. M. Brown",
            "year": 2013,
            "title": "Architectural Analysis and Predicted Functional Capability of the Human Latissimus Dorsi Muscle."
        },
        {
            "authors": "Schoenfeld, Brad J, and Jozo Grgic",
            "year": 2020,
            "title": "Effects of Range of Motion on Muscle Development during Resistance Training Interventions: A Systematic Review."
        },
        {
            "authors": "Oranchuk, Dustin J., et al.",
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
    "vector_db": "workout_exercises_db",
    "textfile_name": "best_shoulder_exercises_Legion.txt",
    "reviewers": [],
    "references": [
        {
            "authors": "Saeterbakken, Atle H., and Marius S. Fimland",
            "year": 2013,
            "title": "Effects of Body Position and Loading Modality on Muscle Activity and Strength in Shoulder Presses."
        },
        {
            "authors": "Raizada, Shiny, and Amritashish Bagchi",
            "year": 2017,
            "title": "Comparison among the EMG Activity of the Anterior Deltoid and Medial Deltoid during Two Variations of Dumbbell Shoulder Press Exercise."
        },
        {
            "authors": "Schoenfeld, Brad J, et al.",
            "year": 2011,
            "title": "The Upright Row: Implications for Preventing Subacromial Impingement."
        },
        {
            "authors": "Page, Phil",
            "year": 2011,
            "title": "Shoulder Muscle Imbalance and Subacromial Impingement Syndrome in Overhead Athletes."
        },
        {
            "authors": "Franke, Rodrigo, et al.",
            "year": 2014,
            "title": "Analysis of Anterior, Middle and Posterior Deltoid Activation during Single and Multijoint Exercises."
        }
    ]
},
{
    "title": "The Best Arm Workouts for Building Mass",
    "author": "Michael Matthews",
    "publication_date": "2024-04-30",
    "url": "https://legionathletics.com/best-arm-exercises/",
    "vector_db": "workout_exercises_db",
    "textfile_name": "best_arm_exercises_Legion.txt",
    "reviewers": [],
    "references": [
        {
            "authors": "Kholinne, Erica, et al.",
            "year": 2018,
            "title": "The Different Role of Each Head of the Triceps Brachii Muscle in Elbow Extension."
        },
        {
            "authors": "Gentil, Paulo, et al.",
            "year": 2015,
            "title": "Single vs. Multi-Joint Resistance Exercises: Effects on Muscle Strength and Hypertrophy."
        },
        {
            "authors": "Youdas, James W, et al.",
            "year": 2010,
            "title": "Surface Electromyographic Activation Patterns and Elbow Joint Motion during a Pull-Up, Chin-Up, or Perfect-PullupTM Rotational Exercise."
        },
        {
            "authors": "de França, Henrique Silvestre, et al.",
            "year": 2015,
            "title": "The Effects of Adding Single-Joint Exercises to a Multi-Joint Exercise Resistance Training Program on Upper Body Muscle Strength and Size in Trained Men."
        },
        {
            "authors": "Oliveira, Liliam F., et al.",
            "year": 2009,
            "title": "Effect of the Shoulder Position on the Biceps Brachii Emg in Different Dumbbell Curls."
        }
    ]
},
{
    "title": "Leg Day Workout Routine for Hypertrophy & Building Mass",
    "author": "Michael Matthews",
    "publication_date": "2024-03-19",
    "url": "https://legionathletics.com/leg-workouts/",
    "vector_db": "workout_exercises_db",
    "textfile_name": "best_leg_exercises_Legion.txt",
    "reviewers":[],
    "references": [
        {
            "authors": "Yavuz, Hasan Ulas, et al.",
            "year": 2015,
            "title": "Kinematic and EMG Activities during Front and Back Squat Variations in Maximum Loads."
        },
        {
            "authors": "Gullett, Jonathan C, et al.",
            "year": 2009,
            "title": "A Biomechanical Comparison of Back and Front Squats in Healthy Trained Individuals."
        },
        {
            "authors": "Jones, Margaret T, et al.",
            "year": 2012,
            "title": "Effects of Unilateral and Bilateral Lower-Body Heavy Resistance Exercise on Muscle Activity and Testosterone Responses."
        },
        {
            "authors": "DeFOREST, Bradley A., et al.",
            "year": 2014,
            "title": "Muscle Activity in Single- vs. Double-Leg Squats."
        },
        {
            "authors": "Wojtys, E M, et al.",
            "year": 1996,
            "title": "Neuromuscular Adaptations in Isokinetic, Isotonic, and Agility Training Programs."
        },
        {
            "authors": "Gentil, Paulo, et al.",
            "year": 2015,
            "title": "Single vs. Multi-Joint Resistance Exercises: Effects on Muscle Strength and Hypertrophy."
        },
        {
            "authors": "Schoenfeld, Brad J.",
            "year": 2010,
            "title": "The Mechanisms of Muscle Hypertrophy and Their Application to Resistance Training."
        },
        {
            "authors": "Gonzalez, Adam M., et al.",
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
    "vector_db": "workout_exercises_db",
    "textfile_name": "best_core_exercises_Legion.txt",
    "reviewers":[],
    "references": [
        {
            "authors": "Vispute, Sachin S, et al.",
            "year": 2011,
            "title": "The Effect of Abdominal Exercise on Abdominal Fat."
        },
        {
            "authors": "Stallknecht, Bente, et al.",
            "year": 2007,
            "title": "Are Blood Flow and Lipolysis in Subcutaneous Adipose Tissue Influenced by Contractions in Adjacent Muscles in Humans?"
        },
        {
            "authors": "Nuzzo, James L, et al.",
            "year": 2008,
            "title": "Trunk Muscle Activity during Stability Ball and Free Weight Exercises."
        },
        {
            "authors": "Moraes, Antonio C., et al.",
            "year": 2009,
            "title": "EMG Activation of Abdominal Muscles in the Crunch Exercise Performed with Different External Loads."
        },
        {
            "authors": "SuppVersity EMG Series",
            "year": 2011,
            "title": "Rectus Abdominis, Obliques and Erector Spinae: The Very Best Exercises for Sixpack Abs and a Powerful Midsection."
        },
        {
            "authors": "Francis, P. and Davis, J.",
            "year": 2001,
            "title": "New study puts the crunch on ineffective ab exercises."
        },
        {
            "authors": "Youdas, James W, et al.",
            "year": 2008,
            "title": "An Electromyographic Analysis of the Ab-Slide Exercise, Abdominal Crunch, Supine Double Leg Thrust, and Side Bridge in Healthy Young Adults: Implications for Rehabilitation Professionals."
        }
    ]
},
{
"title": "Hypertrophy Training: How Many Sets Should You Do To Maximize Muscle Growth?",
"author": "John Fawkes",
"publication_date": "2024-01-01",
"url": "https://www.spartan.com/blogs/unbreakable-training/hypertrophy-training",
"vector_db": "workout_sets_db",
"reviewers": [],
"references": [
{
"authors": "Ralston, Grant W., Lon Kilgore, Frank B. Wyatt & Julien S. Baker",
"year": 2017,
"title": "The Effect of Weekly Set Volume on Strength Gain: A Meta-Analysis."
},
{
"authors": "Amirthalingam, Theban, et al.",
"year": 2017,
"title": "Effects of a Modified German Volume Training Program on Muscular Hypertrophy and Strength."
},
{
"authors": "Jones, Andrew M.",
"year": 2025,
"title": "Medicine in Science and Sports Exercise April 2025 - Volume 57 - Issue 4."
},
{
"authors": "Slater, Gary John, et al.",
"year": 2019,
"title": "Is an Energy Surplus Required to Maximize Skeletal Muscle Hypertrophy Associated With Resistance Training."
},
{
"authors": "Vingren, Jakob L., et al.",
"year": 2010,
"title": "Testosterone Physiology in Resistance Exercise and Training: The Upstream Regulatory Elements."
},
{
"authors": "Brodsky, I. G., et al.",
"year": 1996,
"title": "Effects of Testosterone Replacement on Muscle Mass and Muscle Protein Synthesis in Hypogonadal Men--A Clinical Research Center Study."
},
{
"authors": "Urhausen, A., et al.",
"year": 1995,
"title": "Blood Hormones as Markers of Training Stress and Overtraining."
},
{
"authors": "Stults-Kolehmainen, Matthew A., et al.",
"year": 2014,
"title": "Chronic Psychological Stress Impairs Recovery of Muscular Function and Somatic Sensations Over a 96-Hour Period."
}
]
},
{
    "title": "How Many Sets Do You Need?",
    "author": "Jeff Nippard",
    "publication_date": "2025-01-01",
    "url": "https://jeffnippard.com/blogs/news/how-many-sets-do-you-need",
    "vector_db": "workout_sets_db",
    "textfile_name": "how_many_sets_do_you_need_JN.txt",
    "reviewers": [],
    "references": [
        {
            "authors": "Schoenfeld, Brad J., Dan Ogborn, and James W. Krieger",
            "year": 2017,
            "title": "Dose-response relationship between weekly resistance training volume and increases in muscle mass: A systematic review and meta-analysis."
        },
        {
            "authors": "Enes, Alysson, Eduardo O. DE Souza, and Tácito P. Souza-Junior",
            "year": 2022,
            "title": "Effects of Different Weekly Set Progressions on Muscular Adaptations in Trained Males: Is There a Dose-Response Effect?"
        }
    ]
},
{
    "title": "The Top 8 Chest Exercises for Strength and Shape",
    "author": "Travis Edwards",
    "publication_date": "2023-03-29",
    "url": "https://www.healthline.com/health/fitness-exercise/best-chest-exercises",
    "vector_db": "workout_exercises_db",
    "textfile_name": "best_chest_exercises_Heathline.txt",
    "reviewers": [],
    "references": []
},
{
    "title": "The Best Bodyweight Workouts and Exercises You Can Do",
    "author": "Michael Matthews",
    "publication_date": "2019-05-08",
    "url": "https://legionathletics.com/the-ultimate-bodyweight-workout-routine/",
    "vector_db": "workout_exercises_db",
    "textfile_name": "best_bodyweight_exercises_Legion.txt",
    "reviewers": [
        {
            "reviewer": "Brian Grant",
            "qualifications": "Doctor of Physical Therapy (DPT), Orthopedic Residency Graduate in Physical Therapy, Bachelors Degree in Exercise Science , Certified Strength and Conditioning Specialist from the NSCA"
        }
    ],
    "references": []
},
{
    "title": "Top 5 Calf Exercises Without Weights",
    "author": "Caroline Schley",
    "publication_date": "Unknown",
    "url": "https://www.livestrong.com/article/103936-top-calf-exercises-weights/",
    "vector_db": "workout_exercises_db",
    "textfile_name": "best_calf_exercises_Livestrong.txt",
    "reviewers": [
        {
            "reviewer": "Lindsey Elizabeth Cortes",
            "qualifications": "Master of Science (MS), Registered Dietitian (RD), Certified Specialist in Sports Dietetics (CSSD)"
        }
    ],
    "references": []
},
{
  "title": "How Hard Should You Train to Build Muscle?",
  "author": "Jeff Nippard",
  "publication_date": "Unknown",
  "url": "https://jeffnippard.com/blogs/news/how-hard-should-you-train-to-build-muscle",
  "vector_db": "workout_reps_db",
  "textfile_name": "how_hard_should_you_train_JN.txt",
  "reviewers": [],
  "references": [
    {
      "authors": "Zac Robinson, Joshua Pelland, Jacob Remmert and Martin Refalo",
      "year": 2023,
      "title": "Exploring the Dose-Response Relationship Between Estimated Resistance Training Proximity to Failure, Strength Gain, and Muscle Hypertrophy: A Series of Meta-Regressions",
    },
    {
      "authors": "Martin C. Refalo, Eric R. Helms, Zac P. Robinson, D. Lee Hamilton, Jackson J. Fyfe",
      "year": 2024,
      "title": "Similar muscle hypertrophy following eight weeks of resistance training to momentary muscular failure or with repetitions-in-reserve in resistance-trained individuals",

    }
  ]
}
]

def references_init():

    if references_collection.count_documents({}) == 0:
        print("Inserting application references into MongoDB instance...")
        result = references_collection.insert_many(references)

        if len(result.inserted_ids) == len(references):
           print(f"Added application references to MongoDB instance.\n Ids inserted: {result.inserted_ids}")

    else: 
       print("Application references already exist to MongoDB instance.")
            


def get_reference_url(txt_name: str):
  
  document = references_collection.find_one({"textfile_name": txt_name})

  if document:
    if document["url"] is None:
      url = "No url found for source."
    else:
      url = document["url"]
  
  return url

