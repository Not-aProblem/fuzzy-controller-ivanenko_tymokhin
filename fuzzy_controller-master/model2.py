input_lvs = {
    "Small_Breeds": [
        {
            "X": (0, 30, 0.01),
            "name": "Age",
            "terms": {
                "puppy": ("trapmf", 0, 0, 0.4, 1),
                "young": ("trapmf", 0.5, 1, 2, 3),
                "adult": ("trimf", 2.5, 3, 6),
                "senior": ("trapmf", 5, 6, 30, 30),
            },
        },
        {
            "X": (0, 20, 0.01),
            "name": "Weight",
            "terms": {
                "light": ("trapmf", 0, 0, 2, 5),
                "medium": ("trimf", 3, 5, 8),
                "heavy": ("trapmf", 6.5, 10, 20, 20),
            },
        },
        {
            "X": (0, 11, 0.01),
            "name": "Nutrition",
            "terms": {
                "low": ("trapmf", 0, 0, 2, 5),
                "medium": ("trimf", 4, 5, 7),
                "high": ("trapmf", 6, 8, 11, 11),
            },
        },
    ],
    "Medium_Breeds": [
        {
            "X": (0, 30, 0.01),
            "name": "Age",
            "terms": {
                "puppy": ("trapmf", 0, 0, 0.4, 1),
                "young": ("trimf", 0.5, 1, 3),
                "adult": ("trimf", 2, 4, 7),
                "senior": ("trapmf", 5, 7, 30, 30),
            },
        },
        {
            "X": (0, 40, 0.1),
            "name": "Weight",
            "terms": {
                "light": ("trapmf", 0, 0, 3, 8),
                "medium": ("trimf", 5, 8, 12),
                "heavy": ("trapmf", 9, 12, 40, 40),
            },
        },
        {
            "X": (0, 11, 0.01),
            "name": "Nutrition",
            "terms": {
                "low": ("trapmf", 0, 0, 2, 5),
                "medium": ("trimf", 4, 5, 7.5),
                "high": ("trapmf", 6, 8, 11, 11),
            },
        },
    ],
    "Large_Breeds": [
        {
            "X": (0, 30, 0.1),
            "name": "Age",
            "terms": {
                "puppy": ("trapmf", 0, 0, 0.4, 1),
                "young": ("trimf", 0.5, 1, 4),
                "adult": ("trimf", 3, 6, 8),
                "senior": ("trapmf", 7, 9, 30, 30),
            },
        },
        {
            "X": (0, 70, 0.1),
            "name": "Weight",
            "terms": {
                "light": ("trapmf", 0, 0, 5, 15),
                "medium": ("trimf", 10, 15, 25),
                "heavy": ("trapmf", 20, 25, 70, 70),
            },
        },
        {
            "X": (0, 11, 0.01),
            "name": "Nutrition",
            "terms": {
                "low": ("trapmf", 0, 0, 2, 5),
                "medium": ("trimf", 4, 5, 7),
                "high": ("trapmf", 6, 8, 11, 11),
            },
        },
    ],
}


output_lv = {
    "Small_Breeds": {
        "X": (0, 10.1, 0.1),
        "name": "Attractive level",
        "terms": {
            "low": ("trimf", 0, 2, 5),
            "medium": ("trapmf", 3, 5, 6, 7),
            "high": ("trapmf", 6, 7, 10, 10),
        },
    },
    "Medium_Breeds": {
        "X": (0, 10.1, 0.1),
        "name": "Attractive level",
        "terms": {
            "low": ("trimf", 0, 2, 5),
            "medium": ("trapmf", 3, 5, 6, 7),
            "high": ("trapmf", 6, 7, 10, 10),
        },
    },
    "Large_Breeds": {
        "X": (0, 10.1, 0.1),
        "name": "Attractive level",
        "terms": {
            "low": ("trimf", 0, 2, 5),
            "medium": ("trapmf", 3, 5, 6, 7),
            "high": ("trapmf", 6, 7, 10, 10),
        },
    },
}


rule_base = [
    (("puppy", "light", "low"), "high"),
    (("puppy", "light", "medium"), "high"),
    (("puppy", "light", "high"), "high"),
    (("puppy", "medium", "low"), "high"),
    (("puppy", "medium", "medium"), "high"),
    (("puppy", "medium", "high"), "high"),
    (("puppy", "heavy", "low"), "high"),
    (("puppy", "heavy", "medium"), "high"),
    (("puppy", "heavy", "high"), "high"),
    (("young", "light", "low"), "medium"),
    (("young", "light", "medium"), "high"),
    (("young", "light", "high"), "high"),
    (("young", "medium", "low"), "medium"),
    (("young", "medium", "medium"), "high"),
    (("young", "medium", "high"), "high"),
    (("young", "heavy", "low"), "medium"),
    (("young", "heavy", "medium"), "high"),
    (("young", "heavy", "high"), "high"),
    (("adult", "light", "low"), "low"),
    (("adult", "light", "medium"), "medium"),
    (("adult", "light", "high"), "high"),
    (("adult", "medium", "low"), "low"),
    (("adult", "medium", "medium"), "medium"),
    (("adult", "medium", "high"), "high"),
    (("adult", "heavy", "low"), "low"),
    (("adult", "heavy", "medium"), "medium"),
    (("adult", "heavy", "high"), "high"),
    (("senior", "light", "low"), "low"),
    (("senior", "light", "medium"), "low"),
    (("senior", "light", "high"), "medium"),
    (("senior", "medium", "low"), "low"),
    (("senior", "medium", "medium"), "low"),
    (("senior", "medium", "high"), "medium"),
    (("senior", "heavy", "low"), "low"),
    (("senior", "heavy", "medium"), "low"),
    (("senior", "heavy", "high"), "medium"),
]
