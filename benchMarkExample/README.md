# Project Description

### Project Overview
The project is titled [**"Buffalo New Development"**](https://docs.urbanopt.net/resources/example.html) and represents an urban development in Buffalo, NY. This project includes metadata describing the location and context of the development. It is located at latitude 42.813153 and longitude -78.852466, with an elevation of 200 meters above sea level. The time zone is -5.0 (Eastern Time Zone), and CAD coordinates for the site are [0.0, 0.0]. This metadata provides a foundation for urban energy and sustainability analysis within the framework of the project.

---

### Building Details
The **Buffalo New Development** project includes a total of **13 buildings**, each with detailed attributes regarding its use, structure, and geometry.

The first building in the project is **Mixed_use 1**, which is a mixed-use structure built in 2013. It has four stories with a total floor area of 69,664 m² and a footprint area of 17,416 m². The maximum roof height of this building is 14 meters, and it is represented in the GeoJSON file as a polygon geometry.

The second building, **Restaurant 1**, is also classified as mixed-use and was constructed in 2013. It has a single story with a floor area of 2,067 m², which matches its footprint area. The maximum roof height of this building is 3.5 meters, making it a relatively small structure in the development.

**Residential 1** is the third building, constructed in 2013, with three stories. It has a floor area of 11,636 m² and a footprint area of 3,879 m². The building’s maximum roof height is 10.5 meters, and it serves as one of the residential components within the mixed-use urban development.

The fourth building, **Residential 2**, is also a three-story residential building built in 2013. It has a total floor area of 2,929 m² and a footprint area of 976 m². Like Residential 1, it has a maximum roof height of 10.5 meters and is represented as a polygon geometry.

The fifth building, **Residential 3**, is another three-story residential structure built in 2013. It has a total floor area of 3,011 m² and a footprint area of 1,004 m². Its maximum roof height is 10.5 meters, similar to other residential buildings.

**Residential 4** is the sixth building in the project, constructed in 2013. It is a single-story residential structure with a floor area of 815 m² and a footprint area of 815 m². The maximum roof height of this building is 3.5 meters, making it one of the smallest in the project.

The seventh building, **Residential 5**, is also a single-story residential structure built in 2013. It has a floor area of 990 m², which matches its footprint area, and a maximum roof height of 3.5 meters.

**Office 1**, the eighth building, is a six-story mixed-use structure constructed in 2013. It has a substantial floor area of 30,167 m² and a footprint area of 5,028 m². The maximum roof height of this office building is 21 meters, making it one of the taller structures in the project.

The ninth building, **Hospital 1**, is a 10-story mixed-use building constructed in 2013. It has a floor area of 37,343 m² and a footprint area of 3,734 m². With a maximum roof height of 35 meters, it is the tallest building in the development, suitable for complex urban energy simulations.

**Hospital 2** is the tenth building, a three-story mixed-use structure built in 2013. It has a floor area of 26,579 m² and a footprint area of 8,860 m². The maximum roof height is 10.5 meters, contributing to its role in urban energy analysis.

The eleventh building, **Mall 1**, is a three-story mixed-use structure built in 2013. It has a total floor area of 34,679 m² and a footprint area of 11,560 m². The maximum roof height is 10.5 meters, and its size and complexity make it a key feature of the development.

The twelfth building, **Mixed_use 2**, is an eight-story structure built in 2013. It has a large floor area of 118,408 m² and a footprint area of 14,801 m². Its maximum roof height is 28 meters, making it a significant component of the urban development.

Finally, **Residential 6** is the thirteenth building, a 10-story residential structure constructed in 2013. It has a total floor area of 29,284 m² and a footprint area of 2,928 m². With a maximum roof height of 35 meters, it is one of the taller structures in the development and contributes significantly to the residential capacity of the project.


---

### Building Geometry
Each building in the project is represented as a **Polygon** geometry within the GeoJSON file. The polygons define the building footprints using latitude and longitude coordinates, which allow accurate spatial modeling and visualization. These footprints align with the program types described, including mixed-use, residential, office, and mall structures. The attached image provides a visual representation of these geometries, illustrating the distribution of different program types across the site. This level of detail supports comprehensive urban and energy analysis, making the Buffalo New Development project an ideal case study for simulation and optimization.

```json
{
    "mappers": [], 
    "features": [
        {
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.846524472491694, 
                            42.814639324783961
                        ], 
                        [
                            -78.846801456481856, 
                            42.815293235115469
                        ], 
                        [
                            -78.847444584086389, 
                            42.815140681134217
                        ], 
                        [
                            -78.847286133126516, 
                            42.814781238990278
                        ], 
                        [
                            -78.847868010483054, 
                            42.814643212833083
                        ], 
                        [
                            -78.847211099211805, 
                            42.813153000000000
                        ], 
                        [
                            -78.846503420297509, 
                            42.813312599705334
                        ], 
                        [
                            -78.846524472491694, 
                            42.814639324783961
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature", 
            "properties": {
                "number_of_stories": 4, 
                "name": "Mixed_use 1", 
                "year_built": 2013, 
                "floor_height": 3.5, 
                "floor_area": 69664.379738251853, 
                "number_of_stories_above_ground": 4, 
                "building_type": "Mixed use", 
                "type": "Building", 
                "detailed_model_filename": "C:\\Users\\bmohs\\simulation\\Buffalo_New_Development\\hb_json\\Mixed_use_1.json", 
                "id": "Mixed_use_1", 
                "maximum_roof_height": 14.0, 
                "footprint_area": 17416.094934562963
            }
        }, 
        {
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.850630762231489, 
                            42.818578467348068
                        ], 
                        [
                            -78.850389784729970, 
                            42.818031845316277
                        ], 
                        [
                            -78.850012074866996, 
                            42.818121436368351
                        ], 
                        [
                            -78.850253052368501, 
                            42.818668057608171
                        ], 
                        [
                            -78.850630762231489, 
                            42.818578467348068
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature", 
            "properties": {
                "number_of_stories": 1, 
                "name": "Restaurant 1", 
                "year_built": 2013, 
                "floor_height": 3.5, 
                "floor_area": 2066.6820634725736, 
                "number_of_stories_above_ground": 1, 
                "building_type": "Mixed use", 
                "type": "Building", 
                "detailed_model_filename": "C:\\Users\\bmohs\\simulation\\Buffalo_New_Development\\hb_json\\Restaurant_1.json", 
                "id": "Restaurant_1", 
                "maximum_roof_height": 3.5, 
                "footprint_area": 2066.6820634725736
            }
        }, 
        {
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.849298367654768, 
                            42.813370419455389
                        ], 
                        [
                            -78.849832691144101, 
                            42.814562879737615
                        ], 
                        [
                            -78.850156604317249, 
                            42.814484777887621
                        ], 
                        [
                            -78.849622280827901, 
                            42.813292316099421
                        ], 
                        [
                            -78.849298367654768, 
                            42.813370419455389
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature", 
            "properties": {
                "number_of_stories": 3, 
                "name": "Residential 1", 
                "year_built": 2013, 
                "floor_height": 3.5, 
                "floor_area": 11635.558310721039, 
                "number_of_stories_above_ground": 3, 
                "building_type": "Mixed use", 
                "type": "Building", 
                "detailed_model_filename": "C:\\Users\\bmohs\\simulation\\Buffalo_New_Development\\hb_json\\Residential_1.json", 
                "id": "Residential_1", 
                "maximum_roof_height": 10.5, 
                "footprint_area": 3878.5194369070127
            }
        }, 
        {
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.848620933312205, 
                            42.813535834529567
                        ], 
                        [
                            -78.848717252012889, 
                            42.813750791999766
                        ], 
                        [
                            -78.849169537496309, 
                            42.813641735596278
                        ], 
                        [
                            -78.849073218795624, 
                            42.813426777747047
                        ], 
                        [
                            -78.848620933312205, 
                            42.813535834529567
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature", 
            "properties": {
                "number_of_stories": 3, 
                "name": "Residential 2", 
                "year_built": 2013, 
                "floor_height": 3.5, 
                "floor_area": 2928.7344344717771, 
                "number_of_stories_above_ground": 3, 
                "building_type": "Mixed use", 
                "type": "Building", 
                "detailed_model_filename": "C:\\Users\\bmohs\\simulation\\Buffalo_New_Development\\hb_json\\Residential_2.json", 
                "id": "Residential_2", 
                "maximum_roof_height": 10.5, 
                "footprint_area": 976.24481149059238
            }
        }, 
        {
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.848578871552888, 
                            42.813780349961277
                        ], 
                        [
                            -78.848486740621809, 
                            42.813574738581870
                        ], 
                        [
                            -78.848091787101055, 
                            42.813669971048043
                        ], 
                        [
                            -78.848183918032134, 
                            42.813875582110782
                        ], 
                        [
                            -78.848578871552888, 
                            42.813780349961277
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature", 
            "properties": {
                "number_of_stories": 1, 
                "name": "Residential 4", 
                "year_built": 2013, 
                "floor_height": 3.5, 
                "floor_area": 815.42865055911625, 
                "number_of_stories_above_ground": 1, 
                "building_type": "Mixed use", 
                "type": "Building", 
                "detailed_model_filename": "C:\\Users\\bmohs\\simulation\\Buffalo_New_Development\\hb_json\\Residential_4.json", 
                "id": "Residential_4", 
                "maximum_roof_height": 3.5, 
                "footprint_area": 815.42865055911625
            }
        }, 
        {
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.848690428068281, 
                            42.814440088635564
                        ], 
                        [
                            -78.848497790666897, 
                            42.814010177739796
                        ], 
                        [
                            -78.848268462816165, 
                            42.814065473638955
                        ], 
                        [
                            -78.848461100217534, 
                            42.814495384150312
                        ], 
                        [
                            -78.848690428068281, 
                            42.814440088635564
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature", 
            "properties": {
                "number_of_stories": 1, 
                "name": "Residential 5", 
                "year_built": 2013, 
                "floor_height": 3.5, 
                "floor_area": 989.98410910037637, 
                "number_of_stories_above_ground": 1, 
                "building_type": "Mixed use", 
                "type": "Building", 
                "detailed_model_filename": "C:\\Users\\bmohs\\simulation\\Buffalo_New_Development\\hb_json\\Residential_5.json", 
                "id": "Residential_5", 
                "maximum_roof_height": 3.5, 
                "footprint_area": 989.98410910037637
            }
        }, 
        {
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.848542784124930, 
                            42.816176271352944
                        ], 
                        [
                            -78.848356428377954, 
                            42.815760391013860
                        ], 
                        [
                            -78.847152457161528, 
                            42.816050685716974
                        ], 
                        [
                            -78.847338812908504, 
                            42.816466564103742
                        ], 
                        [
                            -78.848542784124930, 
                            42.816176271352944
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature", 
            "properties": {
                "number_of_stories": 6, 
                "name": "Office 1", 
                "year_built": 2013, 
                "floor_height": 3.5, 
                "floor_area": 30166.705903601192, 
                "number_of_stories_above_ground": 6, 
                "building_type": "Mixed use", 
                "type": "Building", 
                "detailed_model_filename": "C:\\Users\\bmohs\\simulation\\Buffalo_New_Development\\hb_json\\Office_1.json", 
                "id": "Office_1", 
                "maximum_roof_height": 21.0, 
                "footprint_area": 5027.7843172668654
            }
        }, 
        {
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.850412370945349, 
                            42.815731994918586
                        ], 
                        [
                            -78.850508689646020, 
                            42.815946944755254
                        ], 
                        [
                            -78.850782609023312, 
                            42.815880898879350
                        ], 
                        [
                            -78.850495658242366, 
                            42.815256273875924
                        ], 
                        [
                            -78.849739696176059, 
                            42.815443726523824
                        ], 
                        [
                            -78.849917587820173, 
                            42.815856472123379
                        ], 
                        [
                            -78.850412370945349, 
                            42.815731994918586
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature", 
            "properties": {
                "number_of_stories": 10, 
                "name": "Hospital 1", 
                "year_built": 2013, 
                "floor_height": 3.5, 
                "floor_area": 37343.302500468475, 
                "number_of_stories_above_ground": 10, 
                "building_type": "Mixed use", 
                "type": "Building", 
                "detailed_model_filename": "C:\\Users\\bmohs\\simulation\\Buffalo_New_Development\\hb_json\\Hospital_1.json", 
                "id": "Hospital_1", 
                "maximum_roof_height": 35.0, 
                "footprint_area": 3734.3302500468471
            }
        }, 
        {
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.850560422836892, 
                            42.816075714653479
                        ], 
                        [
                            -78.850725714122547, 
                            42.816450230600942
                        ], 
                        [
                            -78.849401375191619, 
                            42.816771188127689
                        ], 
                        [
                            -78.849580181807681, 
                            42.817168171015553
                        ], 
                        [
                            -78.850726244343946, 
                            42.816890421189918
                        ], 
                        [
                            -78.850856611801063, 
                            42.817195539033875
                        ], 
                        [
                            -78.851321403829687, 
                            42.817082896249232
                        ], 
                        [
                            -78.850836310373424, 
                            42.816006367205702
                        ], 
                        [
                            -78.850560422836892, 
                            42.816075714653479
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature", 
            "properties": {
                "number_of_stories": 3, 
                "name": "Hospital 2", 
                "year_built": 2013, 
                "floor_height": 3.5, 
                "floor_area": 26579.255972810512, 
                "number_of_stories_above_ground": 3, 
                "building_type": "Mixed use", 
                "type": "Building", 
                "detailed_model_filename": "C:\\Users\\bmohs\\simulation\\Buffalo_New_Development\\hb_json\\Hospital_2.json", 
                "id": "Hospital_2", 
                "maximum_roof_height": 10.5, 
                "footprint_area": 8859.7519909368366
            }
        }, 
        {
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.850605555771011, 
                            42.819475318345170
                        ], 
                        [
                            -78.850823933670512, 
                            42.819978743090559
                        ], 
                        [
                            -78.852466000000007, 
                            42.819582842193583
                        ], 
                        [
                            -78.851634872399458, 
                            42.817744251342589
                        ], 
                        [
                            -78.851152678318570, 
                            42.817860511674979
                        ], 
                        [
                            -78.851745680647682, 
                            42.819204415920488
                        ], 
                        [
                            -78.850605555771011, 
                            42.819475318345170
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature", 
            "properties": {
                "number_of_stories": 8, 
                "name": "Mixed use 2", 
                "year_built": 2013, 
                "floor_height": 3.5, 
                "floor_area": 118408.20202497626, 
                "number_of_stories_above_ground": 8, 
                "building_type": "Mixed use", 
                "type": "Building", 
                "detailed_model_filename": "C:\\Users\\bmohs\\simulation\\Buffalo_New_Development\\hb_json\\Mixed_use_2.json", 
                "id": "Mixed_use_2", 
                "maximum_roof_height": 28.0, 
                "footprint_area": 14801.025253122032
            }
        }, 
        {
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.849050324610602, 
                            42.814505271989326
                        ], 
                        [
                            -78.849146643311300, 
                            42.814720226089911
                        ], 
                        [
                            -78.849611669230868, 
                            42.814608099429982
                        ], 
                        [
                            -78.849515350530211, 
                            42.814393144939686
                        ], 
                        [
                            -78.849050324610602, 
                            42.814505271989326
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature", 
            "properties": {
                "number_of_stories": 3, 
                "name": "Residential 3", 
                "year_built": 2013, 
                "floor_height": 3.5, 
                "floor_area": 3011.1868676352533, 
                "number_of_stories_above_ground": 3, 
                "building_type": "Mixed use", 
                "type": "Building", 
                "detailed_model_filename": "C:\\Users\\bmohs\\simulation\\Buffalo_New_Development\\hb_json\\Residential_3.json", 
                "id": "Residential_3", 
                "maximum_roof_height": 10.5, 
                "footprint_area": 1003.7289558784178
            }
        }, 
        {
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.849153004130457, 
                            42.819007348715132
                        ], 
                        [
                            -78.848263103091497, 
                            42.817021468986489
                        ], 
                        [
                            -78.847683413246500, 
                            42.817161237829950
                        ], 
                        [
                            -78.848573314285488, 
                            42.819147113069896
                        ], 
                        [
                            -78.849153004130457, 
                            42.819007348715132
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature", 
            "properties": {
                "number_of_stories": 3, 
                "name": "Mall 1", 
                "year_built": 2013, 
                "floor_height": 3.5, 
                "floor_area": 34678.680435793278, 
                "number_of_stories_above_ground": 3, 
                "building_type": "Mixed use", 
                "type": "Building", 
                "detailed_model_filename": "C:\\Users\\bmohs\\simulation\\Buffalo_New_Development\\hb_json\\Mall_1.json", 
                "id": "Mall_1", 
                "maximum_roof_height": 10.5, 
                "footprint_area": 11559.560145264426
            }
        }, 
        {
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.848910927541823, 
                            42.819892858331379
                        ], 
                        [
                            -78.849138957205341, 
                            42.820389251168244
                        ], 
                        [
                            -78.849723570853229, 
                            42.820244766054003
                        ], 
                        [
                            -78.849495541189711, 
                            42.819748372057155
                        ], 
                        [
                            -78.848910927541823, 
                            42.819892858331379
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature", 
            "properties": {
                "number_of_stories": 10, 
                "name": "Residential 6", 
                "year_built": 2013, 
                "floor_height": 3.5, 
                "floor_area": 29284.275439740886, 
                "number_of_stories_above_ground": 10, 
                "building_type": "Mixed use", 
                "type": "Building", 
                "detailed_model_filename": "C:\\Users\\bmohs\\simulation\\Buffalo_New_Development\\hb_json\\Residential_6.json", 
                "id": "Residential_6", 
                "maximum_roof_height": 35.0, 
                "footprint_area": 2928.4275439740886
            }
        }
    ], 
    "type": "FeatureCollection", 
    "project": {
        "cad_coordinates": [
            0.0, 
            0.0
        ], 
        "longitude": -78.852466000000007, 
        "elevation": 200.0, 
        "latitude": 42.813153000000000, 
        "city": "Buffalo, NY", 
        "country": "-", 
        "name": "Buffalo New Development", 
        "time_zone": -5.0, 
        "id": "Buffalo_New_Development"
    }
}
```

---
# Program type
The image below represents the program types of the buildings included in the **Buffalo New Development** project. Each building is color-coded to reflect its designated program type, allowing for quick visual identification of the functional classification of the structures. The program types include **StripMall Building** (red), **Outpatient Building** (orange), **Mixed Use Building Program** (yellow), **MidriseApartment Building** (light blue), **MediumOffice Building** (blue), and **FullServiceRestaurant Building** (dark blue). These program types correspond to the specific purposes of the buildings, such as retail, healthcare, residential, office spaces, and dining. The distribution of these programs highlights the mixed-use nature of the development, promoting a balance of residential, commercial, and service-oriented functions to support the community's needs and energy analysis.

<img width="503" alt="benchmark_1" src="https://github.com/user-attachments/assets/291050d1-2c33-4b73-8930-5b445ffc5500" />

---
# Results

### Energy Flow Simulation Results (EUI in kWh/m²)

The table below summarizes the results of the energy flow simulation, showing the End Use Intensity (EUI) for various end uses in the building. The values represent the energy consumed per square meter of gross floor area for each category.

| End Use               | EUI (kWh/m²) |
|-----------------------|--------------|
| Heating              | 65.162       |
| Cooling              | 14.075       |
| Interior Lighting    | 33.634       |
| Electric Equipment   | 38.411       |
| VAV System Fans      | 3.565        |
| Pumps                | 3.924        |
| Heat Rejection       | 0.680        |
| Gas Equipment        | 3.962        |
| Water Systems        | 6.797        |
| Fans                 | 1.451        |

### Description of Results
The simulation results indicate that **heating** has the highest energy use intensity, consuming 65.162 kWh/m². This suggests significant energy demands for maintaining thermal comfort during colder months. **Electric equipment** (38.411 kWh/m²) and **interior lighting** (33.634 kWh/m²) are also major contributors to overall energy consumption, likely due to building usage patterns and operational requirements.

Cooling systems, represented by **cooling** (14.075 kWh/m²) and **water systems** (6.797 kWh/m²), contribute a moderate amount to the energy usage. Ancillary systems, such as **VAV system fans** (3.565 kWh/m²), **pumps** (3.924 kWh/m²), and **gas equipment** (3.962 kWh/m²), show relatively low energy demands. **Heat rejection** and **fans** have the lowest EUI values, at 0.680 kWh/m² and 1.451 kWh/m² respectively, indicating minor contributions to the overall energy profile.

These results provide a detailed breakdown of energy consumption patterns, enabling targeted interventions for energy efficiency improvements.
