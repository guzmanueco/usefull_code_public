udemy course: https://www.udemy.com/course/yaml-zero-to-master/

# What is YAML?

- It is a light-weight, human-readable data-serialization language.
- Primarily designed to make forat easy to read includng adavnced features in comparision with JSON and XML.
- Similar to JSON and XML with minimal syntax and similar capabilities.
- Similar inline style to JSON.
- YAML supports comments, while JSON does not.
- It makes very easy to represent complex mappings.


# YAML vs JSON vs XML
- XML --> JSON --> YAML: this was the order of appearance
- XML: pretty much ued as data exchange format in web services.
- JSON: appeared to simplify data exchange format for app services, mobile apps and web services.
- YAML: appeared because of the need of having to write the configuration files in a huma readable format (since they have to be updated by humans). It can be used for data exchange, but it is mainly used for devops configuration files.
- YAML is a super set JSON, it includes all JSON features plus extra features.


# YAML advantages 
- Easier to read than XML and JSON.
- Minimalist syntax.
- Allows comments.
- Hierarchy is denoted using double space charachters isntead of <> as in XML or {} as in JSON.
- Lighter than XML and JSON.
- Allows data transfering between applications, but it is mostly used for configuration files, since JSON is already light enough for data transfering.
- Used in Docker, Kubernetes, Azure, AWS, GCP, GitHub, Jenkins...

# YAML Text Editor
One of the best options is Atom Text Editor. Detect YAML syntax errors!
Installation: 
- Package: https://atom.io/
- Install packages: https://atom.io/packages/linter-js-yaml
- Help: https://apple.stackexchange.com/questions/131348/how-to-make-command-apm-available-after-installing-atom


# YAML Syntax
- Kay-value pairs: <Key>: <Value>
- Arrays:
    <ArrayName>:
      - <Element1>
      - <Element2>
- Identation: double spaces. IT DOES NOT INCLUDE TABS
- YAML is CASE SENSITIVE


# Scalars in YAML
- Inside a KeyValue pair, a Scalar represents a single value
    Ex: <name: eazybytes>, <eazybytes> is the single stored value
- Scalar supports integer, float, Boolean, String...
- To see type of scalars examples go to YAML/2 YAML Basic Concepts/scalar_examples.yaml


# Strings inside YAML
- Strings don't need explicit double or single quotes.
    Ex: Java='Java'="Java" are the same to YAML
- Quotes are useful for strings containing special characters.
- "Yes" and "No" should also be in quotes, since they are interpreted as Boolean values by YAML.
- Two styles
    A) Folded style: uses > character to remove newlines within the string
    B) Literal style: uses | to turn every newline within the string into a literal newline
  So, if you use the > YAML will ignore the newline, if you use the |, YAML will preserve the newline.
- For examples, refer to YAML/2 YAML Basic Concepts/string_examples.yaml


# Comments in YAML
YAML provides comment using the "#" symbol. It does not provide multiline comments, though, so in each line we want to write a comment at, we nee to use "#".


# Implicit and Explicit Typing in YAML
- YAML offers versatility in typing by autodetecting data types.
- It also supports explicit typing. See YAML/2 YAML Basic Concepts/explicit_typing_examples.yaml


# TimeStamp and DateTime in YAML
- Explicitly types by using !!timestamp
        Formats:
            canonical: 2001-12-15T02:59:43.1Z
            iso8601: 2001-12-14t21:59:43.10 -5
            space separated: 2001-12-14 21:59:43.10 -5
            no time zone(Z): 2001-12-15 2:59:43.10
            date(00:00:00Z): 2002-12-14
- For examples see YAML/2 YAML Basic Concepts/date_type_examples.yaml


# Sequencies/Collections in YAML
- These are like list/arrays that accept several key/values
- We can assemble a sequence within another sequence
- Refer to YAML/2 YAML Basic Concepts/sequences_examples.yaml


# Dictionaries inside YAML
- They're sequences of key-value pairs
- See YAML/2 YAML Basic Concepts/dictionaries_examples.yaml


# Complex Keys in YAML
- There can be complex keys, such as multi-line strings.
- We use ? followed by a space to indicate the start of a complex key.
- Refer to YAML/3 YAML Complex Concepts/complex_keys_examples.yaml


# Anchors and Alias in YAML
- Anchors are identified by &
- Alias are identified by *
- Refer to YAML/3 YAML Complex Concepts/anchors_and_alias_examples.yaml


# Overriding and Merging in YAML
- After defining anchor values in a YAML file, what if you want essentially the same block of code with one small change?
- You can override with '<<' character: before the Alias to add more values, or override existing ones.
- When using overrides, mapping are overriden if the new mapping has the same name or is added afterward if different.
Overriding is also called merge.
- Refer to YAML/3 YAML Complex Concepts/override_examples.yaml


# Multidocument in YAML
- You can refer the start of a document with ---
- You can refer the end of a document with ...
- Refer to YAML/3 YAML Complex Concepts/multidocument_examples.yaml


# Validate YAML files with yamllint
- Installation: pip install yamllint
- Usage: yamllint <filename>