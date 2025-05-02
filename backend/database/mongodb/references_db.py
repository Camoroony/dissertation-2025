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
    "textfile_name": "best_chest_exercises_Healthline.txt",
    "reviewers": [
        {
            "reviewer": "Daniel Bubnis",
            "qualifications": ("Associate's Degree (AA) - Pennsylvania State University, Bachelor's Degree (BA) - Marywood University, Master's Degree (MS) – California University of Pennsylvania, "
            "NASM Certified Personal Trainer (NASM-CPT), NASE Level II Certified Speed Specialist (NASE Level II-CSS)")
        }
    ],
    "references": []
},
{
    "title": "21 Bodyweight Core Exercises You Might Want to Try at Home",
    "author": "Greatist.com team",
    "publication_date": "2024-10-25",
    "url": "https://greatist.com/move/best-bodyweight-exercises-abs",
    "vector_db": "workout_exercises_db",
    "textfile_name": "bodyweight_core_exercises_greatist.txt",
    "reviewers": [
        {
            "reviewer": "Daniel Bubnis",
            "qualifications": ("Associate's Degree (AA) - Pennsylvania State University, Bachelor's Degree (BA) - Marywood University, Master's Degree (MS) – California University of Pennsylvania, "
            "NASM Certified Personal Trainer (NASM-CPT), NASE Level II Certified Speed Specialist (NASE Level II-CSS)")
        }
    ],
    "references": []
},
{
    "title": "9 Bodyweight Leg Exercises for Every Body",
    "author": "Tyler Read",
    "publication_date": "2021-02-26",
    "url": "https://www.healthline.com/nutrition/bodyweight-leg-exercises",
    "vector_db": "workout_exercises_db",
    "textfile_name": "bodyweight_leg_exercises_Healthline.txt",
    "reviewers": [
        {
            "reviewer": "Daniel Bubnis",
            "qualifications": ("Associate's Degree (AA) - Pennsylvania State University, Bachelor's Degree (BA) - Marywood University, Master's Degree (MS) – California University of Pennsylvania, "
            "NASM Certified Personal Trainer (NASM-CPT), NASE Level II Certified Speed Specialist (NASE Level II-CSS)")
        }
    ],
    "references": []
},
{
    "title": "Bodyweight Hamstring Exercises for Every Experience Level",
    "author": "Katey Davidson",
    "publication_date": "2022-02-21",
    "url": "https://www.healthline.com/nutrition/bodyweight-leg-exercises",
    "vector_db": "workout_exercises_db",
    "textfile_name": "bodyweight_hamstring_exercises_Healthline.txt",
    "reviewers": [
        {
            "reviewer": "Daniel Bubnis",
            "qualifications": ("Associate's Degree (AA) - Pennsylvania State University, Bachelor's Degree (BA) - Marywood University, Master's Degree (MS) – California University of Pennsylvania, "
            "NASM Certified Personal Trainer (NASM-CPT), NASE Level II Certified Speed Specialist (NASE Level II-CSS)")
        }
    ],
    "references": []
},
{
    "title": "No More Backaches: 18 Exercises for a Stronger Back",
    "author": "Nicole Davis and Katey Davidson",
    "publication_date": "2024-04-10",
    "url": "https://www.healthline.com/health/fitness/back-strengthening-muscles-posture",
    "vector_db": "workout_exercises_db",
    "textfile_name": "best_back_exercises_Healthline.txt",
    "reviewers": [
      {
  "reviewer": "Gregory Minnis, DPT",
  "qualifications": "Bachelor of Science (BS) – University of Delaware, Doctor of Physical Therapy (DPT) – University of St. Augustine, Licensed Physical Therapist – State of California and State of New Jersey, CPR Certified, Completed advanced certification in evaluation and treatment of the temporomandibular joint (TMJ)"
}
    ],
"references": [
  {
    "authors": "MedlinePlus",
    "year": 2017,
    "title": "Guide to good posture"
  },
  {
    "authors": "World Health Organization (WHO)",
    "year": 2023,
    "title": "Low back pain"
  },
  {
    "authors": "Tataryn N, Simas V, Furness J, Climstein M",
    "year": 2021,
    "title": "Posterior-chain resistance training compared to general exercise and walking programmes for the treatment of chronic low back pain in the general population: A systematic review and meta-analysis"
  }
]
},
{
    "title": "30 Dumbbell Exercises To Love Leg Day",
    "author": "Eryn Barber",
    "publication_date": "2022-06-20",
    "url": "https://mirafit.co.uk/blog/30-dumbbell-exercises-to-love-leg-day/",
    "vector_db": "workout_exercises_db",
    "textfile_name": "dumbbell_leg_exercises_mf.txt",
    "reviewers": [
  {
    "reviewer": "Eryn Barber",
    "qualifications": "Master of Science (MSc) in Strength & Conditioning, Level 3 Personal Trainer, Level 3 Yoga Teacher, Pre-Natal & Post-Natal Training Specialist"
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
    "authors": "MedlinePlus",
    "year": 2017,
    "title": "Guide to good posture"
  },
  {
    "authors": "World Health Organization (WHO)",
    "year": 2023,
    "title": "Low back pain",
  },
  {
    "authors": "Tataryn N, Simas V, Furness J, Climstein M",
    "year": 2021,
    "title": "Posterior-chain resistance training compared to general exercise and walking programmes for the treatment of chronic low back pain in the general population: A systematic review and meta-analysis"
  }
]
},
{
  "title": "Strength and Conditioning Terminology",
  "author": "Abobakr Ravand",
  "publication_date": "2022-07-21",
  "url": "https://iascfitness.org/strength-conditioning-terminology/",
  "vector_db": "overall_db",
  "textfile_name": "s_and_c_terminology_AR.txt",
  "reviewers": [],
  "references": [
    {
      "authors": "Zatsiorsky, V.M. and Kraemer, W.J.",
      "year": 2004,
      "title": "Science and Practice of Strength Training"
    },
    {
      "authors": "Verkhoshansky, Y. and Verkhoshansky, N.",
      "year": 2011,
      "title": "Special Strength Training Manual for Coaches"
    },
    {
      "authors": "Kraemer, W.J., Deschenes, M.R. and Fleck, S.J.",
      "year": 1988,
      "title": "Physiological adaptations to resistance exercise. Implications for athletic conditioning"
    },
    {
      "authors": "Bird, S.P., Tarpenning, K.M. and Marino, F.E.",
      "year": 2005,
      "title": "Designing Resistance Training Programmes to Enhance Muscular Fitness"
    },
    {
      "authors": "Kraemer, W.J. and Ratamess, N.A.",
      "year": 2004,
      "title": "Fundamentals of resistance training: progression and exercise prescription"
    },
    {
      "authors": "Fleck, S.J. and Kraemer, W.J.",
      "year": "Unknown",
      "title": "Designing Resistance Training Programs (Fourth Edition)"
    }
  ]
},
{
  "title": "What is Hypertrophy?",
  "author": "NSCA (National Strength and Conditioning Association)",
  "publication_date": "Unknown",
  "url": "https://www.nsca.com/contentassets/d27e2ba7e56949229d3eb1aaef7ddcfa/trainertips_hypertrophy_201601.pdf?srsltid=AfmBOoq-pT_RG3v3V0d3xg1WPob_nrN1aGhd5CFAFs69ada5-nj9AP_Z",
  "vector_db": "overall_db",
  "textfile_name": "what_is_hypertrophy_NSCA.txt",
  "reviewers": [],
  "references": [
    {
      "authors": "Schoenfeld, B. J.",
      "year": 2010,
      "title": "The Mechanisms of Muscle Hypertrophy and Their Application to Resistance Training"
    },
    {
      "authors": "Schoenfeld, B.",
      "year": 2011,
      "title": "The Use of Specialized Training to Maximize Muscle Hypertrophy"
    },
    {
      "authors": "Spano, M.",
      "year": 2012,
      "title": "Nutrition in the Personal Training Setting. In NSCA’s Essentials of Personal Training (2nd ed.)"
    },
    {
      "authors": "Weir, J. P. and Brown, L. E.",
      "year": 2012,
      "title": "Resistance Training Adaptations. In NSCA’s Essentials of Personal Training (2nd ed.)"
    },
    {
      "authors": "Kubitz, K., Landers, D., Petruzzello, S., and Han, M.",
      "year": 1996,
      "title": "The Effects of Acute and Chronic Exercise on Sleep: A Meta-Analytic Review"
    }
  ]
},
{
  "title": "Hypertrophy Training: The Complete Guide (Plus Workouts)",
  "author": "Eric Curry",
  "publication_date": "2025-03-17",
  "url": "https://www.scienceforsport.com/hypertrophy-training/?srsltid=AfmBOopn6y7pGws_w83X4Ing08CGNvvf2IeTvcUdt5_tN4XQF3keWLRU",
  "vector_db": "overall_db",
  "textfile_name": "hypertrophy_guide_SFS.txt",
  "reviewers": [],
 "references": [
  {
    "authors": "Haff, G. G., & Triplett, N. T. (Eds.)",
    "year": 2015,
    "title": "Essentials of strength training and conditioning (4th ed.)"
  },
  {
    "authors": "Schoenfeld, B. J.",
    "year": 2010,
    "title": "The mechanisms of muscle hypertrophy and their application to resistance training"
  },
  {
    "authors": "Taber, C. B., Vigotsky, A., Nuckols, G., & Haun, C. T.",
    "year": 2019,
    "title": "Exercise-induced myofibrillar hypertrophy is a contributory cause of gains in muscle strength"
  },
  {
    "authors": "Karki, G.",
    "year": 2018,
    "title": "Muscle-skeletal muscle-gross and ultra structure"
  },
  {
    "authors": "Tamaki, T., Akatsuka, A., Tokunaga, M., Ishige, K., Uchiyama, S., & Shiraishi, T.",
    "year": 1997,
    "title": "Morphological and biochemical evidence of muscle hyperplasia following weight-lifting exercise in rats"
  },
  {
    "authors": "Schoenfeld, B.",
    "year": 2021,
    "title": "Science and development of muscle hypertrophy"
  },
  {
    "authors": "Churchward-Venne, T. A., Murphy, C. H., Longland, T. M., & Phillips, S. M.",
    "year": 2013,
    "title": "Role of protein and amino acids in promoting lean mass accretion with resistance exercise and attenuating lean mass loss during energy deficit in humans"
  },
  {
    "authors": "Figueiredo, V. C.",
    "year": 2019,
    "title": "Revisiting the roles of protein synthesis during skeletal muscle hypertrophy induced by exercise"
  },
  {
    "authors": "Garlick, P. J.",
    "year": 2005,
    "title": "The role of leucine in the regulation of protein metabolism"
  },
  {
    "authors": "Rondanelli, M., Nichetti, M., Peroni, G., Faliva, M. A., Naso, M., Gasparri, C., Perna, S., Oberto, L., Di Paolo, E., Riva, A., Petrangolini, G., Guerreschi, G., & Tartara, A.",
    "year": 2021,
    "title": "Where to find leucine in food and how to feed elderly with sarcopenia in order to counteract loss of muscle mass: Practical advice"
  },
  {
    "authors": "Goldberg, A. L., Etlinger, J. D., Goldspink, D. F., & Jablecki, C.",
    "year": 1975,
    "title": "Mechanism of work-induced hypertrophy of skeletal muscle"
  },
  {
    "authors": "Farthing, J. P., & Chilibeck, P. D.",
    "year": 2003,
    "title": "The effects of eccentric and concentric training at different velocities on muscle hypertrophy"
  },
  {
    "authors": "Smith, R. C., & Rutherford, O. M.",
    "year": 1995,
    "title": "The role of metabolites in strength training. I. A comparison of eccentric and concentric contractions"
  },
  {
    "authors": "Schoenfeld, B., & Grgic, J.",
    "year": 2017,
    "title": "Evidence-based guidelines for resistance training volume to maximize muscle hypertrophy"
  },
  {
    "authors": "Schoenfeld, B. J., Contreras, B., Willardson, J. M., Fontana, F., & Tiryaki-Sonmez, G.",
    "year": 2014,
    "title": "Muscle activation during low- versus high-load resistance training in well-trained men"
  },
  {
    "authors": "Willardson, J. M.",
    "year": 2007,
    "title": "The application of training to failure in periodized multiple-set resistance exercise programs"
  },
  {
    "authors": "Fry, A. C., & Kraemer, W. J.",
    "year": 1997,
    "title": "Resistance exercise overtraining and overreaching"
  },
  {
    "authors": "Haff, G. G.",
    "year": 2000,
    "title": "Roundtable discussion: Machines versus free weights"
  }
]
},
{
    "title": "Top 7 Dumbbell Ab Exercises For Your Core Workout",
    "author": "Erin Lohrenz",
    "publication_date": "2025-01-17",
    "url": "https://endomondo.com/exercise/dumbbell-ab-exercises", 
    "vector_db": "workout_exercises_db",
    "textfile_name": "dumbbell_core_exercises_EM.txt",
    "reviewers": [
        {
            "reviewer": "April Edwards",
            "qualifications": "Master Of Science In Physiotherapy – MSc, Physiotherapy: University of Montreal, Bachelor Of Physiotherapy – BA, Physiotherapy: University Of Montreal"
        }
    ],
    "references": []
}
]

def references_init():

    if references_collection.count_documents({}) == 0:
        print("Inserting application references into MongoDB instance...")
        result = references_collection.insert_many(references)

        if len(result.inserted_ids) == len(references):
           print(f"Added application references to MongoDB instance.\n Ids inserted: {result.inserted_ids}")

    else: 
       print("Application references already exist to MongoDB instance. No need to add reference data.")


def get_reference(txt_name: str):
   
  document = references_collection.find_one({"textfile_name": txt_name}, 
                                            {"_id": 0})

  if document is None:
     raise ValueError(f"No source content found for file: {txt_name}")
  else:
      source = document
  
  return source

def get_references():
   
  references = list(references_collection.find({}, {'_id': 0}))

  if not references:
     raise ValueError(f"No source content found for references collection")
  
  return references
            


def get_reference_url(txt_name: str):
  
  document = references_collection.find_one({"textfile_name": txt_name})

  if document:
    if document["url"] is None:
     raise ValueError(f"No source url found for file: {txt_name}")
    else:
      url = document["url"]
  
  return url

