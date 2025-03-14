import random

def get_determiner(quantity):
    """Return a randomly chosen determiner."""
    determiners = ["one", "the", "a"] if quantity == 1 else ["some", "many", "the"]
    return random.choice(determiners)

def get_noun(quantity):
    """Return a randomly chosen noun."""
    nouns = ["girl", "bird", "child", "car", "rabbit", "dog"] if quantity == 1 else ["girls", "birds", "children", "cars", "rabbits", "dogs"]
    return random.choice(nouns)

def get_verb(quantity, tense):
    """Return a randomly chosen verb."""
    verbs = {
        "past": ["talked", "drank", "laughed", "ran"],
        "present": ["talks", "drinks", "laughs", "runs"] if quantity == 1 else ["talk", "drink", "laugh", "run"],
        "future": ["will talk", "will drink", "will laugh", "will run"]
    }
    return random.choice(verbs[tense])

def get_preposition():
    """Return a randomly chosen preposition."""
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", 
                    "onto", "out", "over", "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase."""
    return f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"

def get_adjective():
    """Return a randomly chosen adjective."""
    adjectives = ["quick", "lazy", "happy", "sad", "red", "blue", "tall", "short"]
    return random.choice(adjectives)

def get_adverb():
    """Return a randomly chosen adverb."""
    adverbs = ["quickly", "slowly", "happily", "sadly", "gracefully", "clumsily", "silently", "loudly"]
    return random.choice(adverbs)

def make_sentence(quantity, tense):
    """Generate a sentence with determiner, noun, verb, adjectives, adverbs, and two prepositional phrases."""
    determiner = get_determiner(quantity).capitalize()
    adjective = get_adjective()
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    adverb = get_adverb()
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    return f"{determiner} {adjective} {noun} {adverb} {verb} {prepositional_phrase1} {prepositional_phrase2}."

def main():
    """Generate and print six sentences with different tenses and quantities."""
    tenses = ["past", "present", "future"]
    for quantity in [1, 2]:
        for tense in tenses:
            print(make_sentence(quantity, tense))

if __name__ == "__main__":
    main()
