| Date              |          |
|:------------------|:---------|
| TODO | Assigned |
| TODO    | Due      |
| Status            | [![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml) |

# BRAND NEW BEAUTIFICATION PROPOSAL PROMPTS `term-world` TENANTS TO TIDY UP

*Reported by `The Reporter` from `TODO`, on `TODO`*

Last week `The Mayor` unveiled a new beautification program in an effort to make `term-world` *the* spot to be. This is the latest in a long line of proposals, projects, programs, and plans that `The Mayor` has been fervently working on to drive both tourism and residency within `term-world`.

This particular program targets the tight-knit communities that lie on the outskirts of our fair `term-world`. The appeal of neighborhoods like `Qermiz` and `Shasha` has gone under the microscope, and according to `The Mayor`, it has been found sorely wanting.

Partnering with `The Landlord` that exercises ownership over these despondent, dismal, and downright depressing domestic hovels, `The Mayor` has decreed that all building exteriors in the targeted communities must meet certain specific "Beautification Standard" metrics, within a week's time. Once the one week grace period is up, `The Mayor` is planning on leveraging his authority as `The Mayor` to evict non-compliant residents.

The Office of the Mayor also commented on a new plan to cultivate domestic agriculture for no other apparent reason than "how hard could it possibly be?!" Whether or not farms will come to festoon the very firmament of term-world seems to be part of the Mayor's Field of Dreams.

## Overview

In this set of activities we cover:

* functions: an essential part of good program design
* comments: writing helpful documentation for yourself and others
* more on variables with a focus on naming and data types
* algorithmic thinking: learning to design programs

### Key facts about your yard

#### The `Luumba.py` (Treehouse)

![Treehouse Diagram visualizing table below](https://user-images.githubusercontent.com/1552764/215453276-7d9aa375-c501-4d0a-8bd4-58c9453c7d05.png)

The dimensions for your treehouse are as follows (it's rectangular):

|Dimension |Measurement       |Number         |Shape |
|:---------|:-----------------|:--------------|:-----|
|Walls |`18` × `27` × `7`     |`4`| Rectangle |
|Roof                         |
|Gables    |`12.73` × `12.73` × `18` |`2` | Triangle |
|Roofing   |`12.73` × `27`    |`2` | Rectangle |
|Cut-outs                     | 
|Windows     | `8` × `3` |`6` | Rectangle |
|Entryway    | `5` × `5`  |`1` | Square |
|Allowance for tree | `4` (radius) | `1` | Circle† |

`†` Use `math.pi` for calculation

Using the above details, you should be able to cobble together (a minimum) `3` functions which represent the shapes you need.

##### This ain't math class

Because this isn't a math test, I'll provide some reminders about formulae used in calculation:

###### Circle

$$ A = \pi r^2 $$

###### Rectangle

$$ A = width \times length$$

###### Triangle

$$ A = \frac{1}{2} \times leg^{2} $$

#### The `Croomba.py` (garden)

Lucky you -- you've been given a garden and all of the responsibilities that come with tending and growing crops. You're allowed to grow whatever `Seed`s you can get from the `SeedCatalog.py`, but you need to figure out what kind of soil creates the best condition for all of your plants. Good thing `term-world` has (i.e. is _in_) the internet.

|Machine |Functionality |
|:-------|:-------------|
|`SeedCatalog.py`|Dispenses `Seed` objects directly to `inventory` |
|`Croomba.py`|Incorporates various agricultral machines to grow `Seed`s into full crops |

See the `Croomba.py` for more details.

This portion of the assignment will also introduce `term-world`'s `inventory` system. This system provides a way for you to transport objects around `term-world`, acquire goods, and (like any good consumer) `use` them. The commands below detail the functionality of the `inventory` system, and you can combine them in the "algorithm" that this section of the assignment requires -- in addition to the short engagement with coding requested above.

#### Inventory

`inventory` is a command that is used to carry different objects around `term-world`. You can only carry `10` object-units in your `inventory` (objects have varying weights).  In order to check whats in your inventory use the command:

```
inventory
```

You will see a screen similar to that below:
![Inventory screen showing three items](https://raw.githubusercontent.com/allegheny-college-cmpsc-100-spr-2023/course-materials/media/img/TW%20-%20Inventory.png)

##### get 

`get` picks up an object from your current location. This commands destroys the objects in its current location. Make sure to use the **file name**.

```
get Tomato.py
```

##### use

If the object is `Consumable`, you can use the `use` command to "use" the object. If It does not have any function then `use` just removes the file. Only uses `1` object at a time.

```
use Tomato
```

##### remove

`remove` gets rid of an object from your `inventory`. You first use the name of the object, then you give the amount of objects you want to delete (If no amount is given then 1 is removed). If you give an amount higher then you have, all objects are removed.

```
remove Tomato 2
```

##### drop

`drop` puts the object in your current location. You first use the name of the object, then you give the amount of objects you want to drop (If no amount is given then 1 is dropped). If you give an amount higher then you have, all objects are droped.

```
drop Tomato 3
```

This command will drop `3` `Tomato.py` files, using sequential numbering to differentiate them:

```
Tomato.py
Tomato1.py
Tomato2.py
```

If any more files are dropped they will continue to follow this numbering pattern. Picking up any of these files will give you a `Tomato` in your inventory.

##### Soil composition chart

The chart below summarizes the percentage of your `inventory` that you'll need to have in order to create the correct soil.

To collect the ingredients for the various soils, head to the `dirt` pile in the `garden` and pick up the correct amount of dirt to try your luck with the `SoilMixer`! Each soil has

|Type |Sand |Silt |Clay |
|:----|:----|:----|:----|
|Sandy|80%   |10%   |10%   |
|Loamy|20%   |30%   |50%   |
|Clay-y|10%  |10%   |80%   |

#### Reflection

The `treehouse` also contains a `reflection.md` document. From this point onward in your experience in `term-world`, you'll be required to answer questions in the file as part of the assignment. Go there and have a look at the questions.

## Access `yard` content

The activities for this week primarily take place in your `yard`. This is the last major structure making up your `home`.

```
                                  ----------
                 ------------     | GARDEN |
                 | WORKSHOP |     ----------
                 ------------       /
                    /              /
----------     ----------      --------
| HOUSE  |     | GARAGE |      | YARD |
---------|     ----------      --------
    |              |              |
    |--------------|--------------|
```


## `term-world Server Backup Policy`

**While we may use this server to store code, you are responsible for using GitHub as your main backup.**

In the event that the `term-world` server goes down for any unforeseen reason, your work may be lost. Though this server is backed up on a regular (i.e., weekly) basis, there is no guarantee that up-to-the-minute data for your work will be restored.

Remember: to err is human; to back up your work is *divine*.
