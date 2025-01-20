# Context

# Integrating OpenStreetMap Data:
To obtain OpenStreetMap (OSM) data for a specific region, go to the [OpenStreetMap website](https://www.openstreetmap.org/). Navigate to the map area of interest and select a bounding box by adjusting the rectangle on the map. The bounding box is defined by four coordinates: top (latitude of the northern edge), bottom (latitude of the southern edge), left (longitude of the western edge), and right (longitude of the eastern edge). These four numbers specify the region you want to export. Once defined, click the "Export" button to download the data in an OSM-compatible format, such as `.osm` or `.pbf`. This exported file can then be fed into an OSM engine (e.g., Osmosis or a custom parser) to retrieve specific features, such as roads, buildings, or amenities, for further analysis or application integration.

For example, the map above shows a portion of the New York region, and the bounding box is defined by the four numbers: top (40.725000), bottom (40.720000), left (-73.985000), and right (-73.980000). You can use these coordinates directly in the URBANO engine within Grasshopper for Rhinoceros to define the area of interest. By inputting these values, URBANO can retrieve and process OSM features such as buildings, roads, and green spaces for urban analysis and simulation tasks. This workflow allows seamless integration of real-world geospatial data into your design and analysis pipeline.

![OpenStreetMap_NewYork](https://github.com/user-attachments/assets/ead26bab-0847-404d-88f8-c6cf8c20450f)
--

# Workflow for Extracting and Integrating OpenStreetMap Data with the URBANO Plugin in Grasshopper

The diagram illustrates the workflow for using the URBANO plugin in Grasshopper to extract specific features, such as buildings, amenities, and streets, from OpenStreetMap (OSM) data. The process begins with **Pulling OSM data** (Step 1), where the user selects a region of interest using the bounding box coordinates (top, bottom, left, and right) from the OSM website. These coordinates define the exact area to be processed. In **Step 2**, the URBANO plugin retrieves specific features, including buildings, amenities, and streets, based on the OSM data for the selected region. Finally, in **Step 3**, the extracted features are "baked" into Grasshopper and Rhinoceros for further use in design and analysis. This seamless process integrates real-world geospatial data into urban planning and simulation tasks.

![Urbano_workflow](https://github.com/user-attachments/assets/41bf4e10-6438-4b4c-b5d8-8e8c009f427a)
---

# Schematic Representation of 3D Buildings and Footprints for BIM Creation:
The image shows a schematic representation of the retrieved buildings from the selected region, based on the OSM data. Each building is represented in 3D, and the schematic also includes the footprints of the buildings. These footprints can be further utilized as a foundation for creating detailed Building Information Models (BIM) of the specific region. By leveraging these footprints, you can enhance the urban planning and architectural design process, enabling accurate modeling and analysis of the built environment.


![new_york_buildings](https://github.com/user-attachments/assets/37b2ab2b-ea3f-4551-ab4e-eb55a41d0d2e)

The image compares [**Dragonfly**](https://github.com/ladybug-tools/dragonfly-core) and [**Honeybee**](https://github.com/ladybug-tools/honeybee-core) models within the context of building energy simulation. The Dragonfly model (shown in the top-right corner) is a simplified representation of buildings, focusing on larger-scale, low-detail massing and zoning. It is used for urban-scale analysis or evaluating energy flows and loads for multiple buildings within a community. On the other hand, the Honeybee model (bottom-right corner) provides more detailed building representations, including individual zones, surfaces, and construction materials, enabling a higher-resolution energy analysis at the building or room level.

### Advantage of Dragonfly for Building Community Simulations:
Dragonfly excels in simulating energy flows for building communities due to its focus on simplified representations, which significantly reduces computational complexity and time. It is well-suited for large-scale analyses involving multiple buildings, where detailed modeling (as in Honeybee) is unnecessary or impractical. Dragonfly allows urban planners and energy analysts to assess energy performance, identify trends, and evaluate the impact of community-level design decisions quickly and effectively.


![difference_between_HB_and_DF](https://github.com/user-attachments/assets/c0deeb42-7c38-4dd7-a614-ce8662a5b914)

# Explaining the difference between DF abd HB

The image highlights three methods for creating urban-scale building community models using Dragonfly, emphasizing its flexibility and streamlined approach to urban energy simulation.

1. **From Rooms-to-Stories-to-Buildings:**
   This method allows detailed modeling of individual rooms, which are then aggregated into stories and subsequently grouped into entire buildings. It provides a high level of control over internal zoning and allows detailed energy simulation for buildings while maintaining the scalability of the model. This method is best suited for projects where the internal organization of buildings impacts energy use significantly.

2. **From Building Solids:**
   This approach uses simplified 3D masses representing entire buildings. These masses capture the geometry and volume of buildings but omit internal zoning details. It is ideal for quickly modeling urban areas where the goal is to assess the energy performance of individual buildings or groups of buildings without delving into internal zone-level details.

3. **From Building Footprints:**
   This method uses 2D building footprint data, such as that retrieved from OpenStreetMap, to create building geometry. Heights and volumes can be assigned to these footprints to generate massing models for urban areas. It is particularly efficient for large-scale simulations where urban energy performance is evaluated based on basic building geometry.

### Features of Dragonfly:
- **Scalability:** Supports modeling of entire urban communities, from individual buildings to city blocks.
- **Simplification:** Reduces computational complexity by allowing flexibility in the level of detail, from highly simplified solids to detailed room-level models.
- **Integration:** Seamlessly connects with other Ladybug Tools for environmental and energy analysis.
- **Adaptability:** Works with data from multiple sources, such as building footprints, 3D solids, or custom-designed room layouts, enabling diverse use cases for urban energy and environmental performance analysis.


![DF_Details](https://github.com/user-attachments/assets/b9ca456d-eb63-4e41-91af-68cba50e563a)

# Explaining how to create a model using DF and explaining how the footprint works

The flow diagram outlines a comprehensive workflow for conducting community-scale energy flow studies using Dragonfly, starting with building footprints obtained from OpenStreetMap (OSM) via the URBANO plugin. The process begins by creating building properties, programs, and construction sets to define the characteristics of the buildings. These inputs are then combined to create building models through the footprint methodology. Afterward, modifications are made to the building models by assigning fenestration (windows and openings) and HVAC systems, ensuring that the buildings are accurately configured for energy analysis.

The refined building models are then used to create a Dragonfly model, which serves as the basis for the community-scale energy simulation. Key inputs such as weather data (retrieved through an EPW file), geographic information (formatted in geoJSON), and simulation configurations are integrated into the Dragonfly model. This model is subsequently run through the **URBANopt engine**, a specialized tool for urban energy modeling. The engine processes the data to simulate energy flows and interactions within the community, providing critical insights into energy performance.

Finally, the energy flow results from the URBANopt engine are passed to a Python-based custom program for scenario analysis. This enables advanced analytics, such as comparing the impact of different design or operational scenarios across specific parts of the community. The results can then be visualized or exported for further study, making this workflow ideal for urban planners and researchers seeking to evaluate energy efficiency and sustainability at the community level.


![FlowChart](https://github.com/user-attachments/assets/29b26486-14a2-4aff-aa21-0d38e0c2c2d9)

# What exactly URBANopt engine needs to run:

### About the Benchmark Project
The [**URBANopt Benchmark project**](https://docs.urbanopt.net/resources/example.html) is an official initiative designed to facilitate large-scale energy flow simulations for urban developments and communities. It integrates tools like URBANopt and Dragonfly to model, analyze, and optimize energy use in complex urban systems. Using the `Buffalo_New_Development.geojson` file as an example, this workflow demonstrates how building-level data, such as geometries, construction types, and energy properties, can be integrated into scalable simulations. By leveraging these features, urban planners and energy analysts can assess energy performance, conduct scenario analyses, and improve the sustainability of urban developments.

### GeoJSON Requirements and Challenges
To run URBANopt simulations, the primary requirement is a valid GeoJSON file. This file encodes spatial and energy-specific attributes for buildings, such as geometry, footprint, floor area, HVAC details, and energy performance data. The `Buffalo_New_Development.geojson` file, available in the linked GitHub directory [Buffalo_New_Development.geojson file](https://github.com/BehnamMohseniGharyehsafa/buildingCommunityEnergyFlowSimulation/tree/main/benchMarkExample), serves as a practical example for such simulations. A significant challenge in formulating GeoJSON files for large-scale models is managing the high level of detail for each building and ensuring compatibility with simulation engines. Automating or standardizing the GeoJSON generation process is key to overcoming this complexity.

### Explanation of the Buffalo GeoJSON File
The `Buffalo_New_Development.geojson` file describes a community-scale development project in Buffalo, NY. It includes metadata like the project's location, time zone, and elevation, along with detailed building data. Each building is represented as a "Feature" within the GeoJSON, with properties such as `floor_area`, `footprint_area`, construction year, number of stories, building type, and geometry coordinates. For example, `"Mixed_use 1"` is a 4-story building with a floor area of 69,664 m² and a detailed model file path provided for further simulation. The file also specifies building geometry in polygons, enabling accurate spatial modeling. Such data allows URBANopt to analyze energy flows and simulate various design or operational scenarios effectively.


```json
{
    "project": {
        "country": "-", 
        "id": "Buffalo_New_Development", 
        "longitude": -78.852466000000007, 
        "elevation": 200.0, 
        "city": "Buffalo, NY", 
        "latitude": 42.813153, 
        "cad_coordinates": [
            0.0, 
            0.0
        ], 
        "name": "Buffalo New Development", 
        "time_zone": -5.0
    }, 
    "mappers": [], 
    "type": "FeatureCollection", 
    "features": [
        {
            "properties": {
                "floor_area": 69664.379738251853, 
                "footprint_area": 17416.094934562963, 
                "year_built": 2013, 
                "number_of_stories_above_ground": 4, 
                "name": "Mixed_use 1", 
                "id": "Mixed_use_1", 
                "detailed_model_filename": "C:\\Users\\22252988\\simulation\\Buffalo_New_Development\\hb_json\\Mixed_use_1.json", 
                "building_type": "Mixed use", 
                "maximum_roof_height": 14.0, 
                "type": "Building", 
                "floor_height": 3.5, 
                "number_of_stories": 4
            }, 
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
                            42.813153
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
            "type": "Feature"
        }, 
        {
            "properties": {
                "floor_area": 2066.6820634725736, 
                "footprint_area": 2066.6820634725736, 
                "year_built": 2013, 
                "number_of_stories_above_ground": 1, 
                "name": "Restaurant 1", 
                "id": "Restaurant_1", 
                "detailed_model_filename": "C:\\Users\\22252988\\simulation\\Buffalo_New_Development\\hb_json\\Restaurant_1.json", 
                "building_type": "Mixed use", 
                "maximum_roof_height": 3.5, 
                "type": "Building", 
                "floor_height": 3.5, 
                "number_of_stories": 1
            }, 
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.850630762231489, 
                            42.818578467348068
                        ], 
                        [
                            -78.85038978472997, 
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
            "type": "Feature"
        }, 
        {
            "properties": {
                "floor_area": 11635.558310721039, 
                "footprint_area": 3878.5194369070127, 
                "year_built": 2013, 
                "number_of_stories_above_ground": 3, 
                "name": "Residential 1", 
                "id": "Residential_1", 
                "detailed_model_filename": "C:\\Users\\22252988\\simulation\\Buffalo_New_Development\\hb_json\\Residential_1.json", 
                "building_type": "Mixed use", 
                "maximum_roof_height": 10.5, 
                "type": "Building", 
                "floor_height": 3.5, 
                "number_of_stories": 3
            }, 
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
            "type": "Feature"
        }, 
        {
            "properties": {
                "floor_area": 2928.7344344717771, 
                "footprint_area": 976.24481149059238, 
                "year_built": 2013, 
                "number_of_stories_above_ground": 3, 
                "name": "Residential 2", 
                "id": "Residential_2", 
                "detailed_model_filename": "C:\\Users\\22252988\\simulation\\Buffalo_New_Development\\hb_json\\Residential_2.json", 
                "building_type": "Mixed use", 
                "maximum_roof_height": 10.5, 
                "type": "Building", 
                "floor_height": 3.5, 
                "number_of_stories": 3
            }, 
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
            "type": "Feature"
        }, 
        {
            "properties": {
                "floor_area": 815.42865055911625, 
                "footprint_area": 815.42865055911625, 
                "year_built": 2013, 
                "number_of_stories_above_ground": 1, 
                "name": "Residential 4", 
                "id": "Residential_4", 
                "detailed_model_filename": "C:\\Users\\22252988\\simulation\\Buffalo_New_Development\\hb_json\\Residential_4.json", 
                "building_type": "Mixed use", 
                "maximum_roof_height": 3.5, 
                "type": "Building", 
                "floor_height": 3.5, 
                "number_of_stories": 1
            }, 
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.848578871552888, 
                            42.813780349961277
                        ], 
                        [
                            -78.848486740621809, 
                            42.81357473858187
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
            "type": "Feature"
        }, 
        {
            "properties": {
                "floor_area": 989.98410910037637, 
                "footprint_area": 989.98410910037637, 
                "year_built": 2013, 
                "number_of_stories_above_ground": 1, 
                "name": "Residential 5", 
                "id": "Residential_5", 
                "detailed_model_filename": "C:\\Users\\22252988\\simulation\\Buffalo_New_Development\\hb_json\\Residential_5.json", 
                "building_type": "Mixed use", 
                "maximum_roof_height": 3.5, 
                "type": "Building", 
                "floor_height": 3.5, 
                "number_of_stories": 1
            }, 
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
            "type": "Feature"
        }, 
        {
            "properties": {
                "floor_area": 30166.705903601192, 
                "footprint_area": 5027.7843172668654, 
                "year_built": 2013, 
                "number_of_stories_above_ground": 6, 
                "name": "Office 1", 
                "id": "Office_1", 
                "detailed_model_filename": "C:\\Users\\22252988\\simulation\\Buffalo_New_Development\\hb_json\\Office_1.json", 
                "building_type": "Mixed use", 
                "maximum_roof_height": 21.0, 
                "type": "Building", 
                "floor_height": 3.5, 
                "number_of_stories": 6
            }, 
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.84854278412493, 
                            42.816176271352944
                        ], 
                        [
                            -78.848356428377954, 
                            42.81576039101386
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
                            -78.84854278412493, 
                            42.816176271352944
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature"
        }, 
        {
            "properties": {
                "floor_area": 37343.302500468475, 
                "footprint_area": 3734.3302500468471, 
                "year_built": 2013, 
                "number_of_stories_above_ground": 10, 
                "name": "Hospital 1", 
                "id": "Hospital_1", 
                "detailed_model_filename": "C:\\Users\\22252988\\simulation\\Buffalo_New_Development\\hb_json\\Hospital_1.json", 
                "building_type": "Mixed use", 
                "maximum_roof_height": 35.0, 
                "type": "Building", 
                "floor_height": 3.5, 
                "number_of_stories": 10
            }, 
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.850412370945349, 
                            42.815731994918586
                        ], 
                        [
                            -78.85050868964602, 
                            42.815946944755254
                        ], 
                        [
                            -78.850782609023312, 
                            42.81588089887935
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
            "type": "Feature"
        }, 
        {
            "properties": {
                "floor_area": 26579.255972810512, 
                "footprint_area": 8859.7519909368366, 
                "year_built": 2013, 
                "number_of_stories_above_ground": 3, 
                "name": "Hospital 2", 
                "id": "Hospital_2", 
                "detailed_model_filename": "C:\\Users\\22252988\\simulation\\Buffalo_New_Development\\hb_json\\Hospital_2.json", 
                "building_type": "Mixed use", 
                "maximum_roof_height": 10.5, 
                "type": "Building", 
                "floor_height": 3.5, 
                "number_of_stories": 3
            }, 
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
            "type": "Feature"
        }, 
        {
            "properties": {
                "floor_area": 118408.20202497626, 
                "footprint_area": 14801.025253122032, 
                "year_built": 2013, 
                "number_of_stories_above_ground": 8, 
                "name": "Mixed use 2", 
                "id": "Mixed_use_2", 
                "detailed_model_filename": "C:\\Users\\22252988\\simulation\\Buffalo_New_Development\\hb_json\\Mixed_use_2.json", 
                "building_type": "Mixed use", 
                "maximum_roof_height": 28.0, 
                "type": "Building", 
                "floor_height": 3.5, 
                "number_of_stories": 8
            }, 
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.850605555771011, 
                            42.81947531834517
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
                            -78.85115267831857, 
                            42.817860511674979
                        ], 
                        [
                            -78.851745680647682, 
                            42.819204415920488
                        ], 
                        [
                            -78.850605555771011, 
                            42.81947531834517
                        ]
                    ]
                ], 
                "type": "Polygon"
            }, 
            "type": "Feature"
        }, 
        {
            "properties": {
                "floor_area": 3011.1868676352533, 
                "footprint_area": 1003.7289558784178, 
                "year_built": 2013, 
                "number_of_stories_above_ground": 3, 
                "name": "Residential 3", 
                "id": "Residential_3", 
                "detailed_model_filename": "C:\\Users\\22252988\\simulation\\Buffalo_New_Development\\hb_json\\Residential_3.json", 
                "building_type": "Mixed use", 
                "maximum_roof_height": 10.5, 
                "type": "Building", 
                "floor_height": 3.5, 
                "number_of_stories": 3
            }, 
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.849050324610602, 
                            42.814505271989326
                        ], 
                        [
                            -78.8491466433113, 
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
            "type": "Feature"
        }, 
        {
            "properties": {
                "floor_area": 34678.680435793278, 
                "footprint_area": 11559.560145264426, 
                "year_built": 2013, 
                "number_of_stories_above_ground": 3, 
                "name": "Mall 1", 
                "id": "Mall_1", 
                "detailed_model_filename": "C:\\Users\\22252988\\simulation\\Buffalo_New_Development\\hb_json\\Mall_1.json", 
                "building_type": "Mixed use", 
                "maximum_roof_height": 10.5, 
                "type": "Building", 
                "floor_height": 3.5, 
                "number_of_stories": 3
            }, 
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
                            -78.8476834132465, 
                            42.81716123782995
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
            "type": "Feature"
        }, 
        {
            "properties": {
                "floor_area": 29284.275439740886, 
                "footprint_area": 2928.4275439740886, 
                "year_built": 2013, 
                "number_of_stories_above_ground": 10, 
                "name": "Residential 6", 
                "id": "Residential_6", 
                "detailed_model_filename": "C:\\Users\\22252988\\simulation\\Buffalo_New_Development\\hb_json\\Residential_6.json", 
                "building_type": "Mixed use", 
                "maximum_roof_height": 35.0, 
                "type": "Building", 
                "floor_height": 3.5, 
                "number_of_stories": 10
            }, 
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
            "type": "Feature"
        }
    ]
}
```

# Explaining the project 

The diagram outlines a comprehensive framework for urban-scale energy modeling and optimization for retrofitted buildings. The system is divided into three main components: **data collection**, **data processing**, and **modeling and output generation**.

The **data collection stage** utilizes tools like URBANO, OpenStreetMap, and plugins for Rhinoceros and Grasshopper to gather geographic and environmental data for a municipality (Mullingar City). These data are used to create parametric 3D building models and assess energy flows at a community scale. In the **data processing stage**, various HVAC configurations such as gas boilers, electric heaters, and air-source heat pumps are modeled, alongside building features like insulation and window ratios, to determine their impact on energy use intensity (EUI). Finally, the **modeling stage** integrates a hybrid Gaussian Process-Deep Learning (GPDL) algorithm to predict EUI and support decision-making for retrofitting scenarios. Outputs include urban-scale EUI assessments, influential retrofitting factors, and fast energy modeling tailored for policymakers and urban planners.

This system demonstrates a scalable and efficient approach, combining traditional building energy modeling tools with advanced techniques to optimize energy efficiency in urban areas.


![FIG_1](https://github.com/user-attachments/assets/26240c81-e718-4fa9-ac20-26e7424a39fb)

---
# HVAC scenario description

The diagram below illustrates a multi-level schematic of different domestic hot water (DHW) and heating systems integrated into a building. The top level represents an **air-source heat pump (HP)** system, which uses ambient air as an energy source to provide both hot water and space heating through radiators. The middle level features an **electric heater and electric DHW system**, where hot water is generated by electric heaters and distributed to radiators and domestic hot water storage. The bottom level showcases a **gas boiler system**, where natural gas is used to generate hot water for space heating and domestic purposes, with exhaust fumes released as a byproduct. Across all levels, the main cold water supply feeds into each system, which then delivers hot water for domestic or radiator use. This setup provides a comparative analysis of energy and water flow for various heating technologies.


![FIG_4](https://github.com/user-attachments/assets/5d8ae7fe-1d49-44b3-b9a4-5df40aa65c23)


---
The bar chart the figure below compares the End Use Intensity (EUI) across three different HVAC systems—**HP and DHW (Heat Pump and Domestic Hot Water)**, **Full Electric**, and **Gas Boiler and DHW**—under the same envelope conditions for cold regions. The EUI is displayed for all four seasons: **Winter**, **Spring**, **Summer**, and **Autumn**.

From the chart, it is evident that **Gas Boiler and DHW** has the highest EUI during **Winter** and **Autumn**, making it the least energy-efficient system during colder seasons. Conversely, **HP and DHW** exhibits the lowest EUI overall, with significantly reduced energy use in **Spring** and **Summer**, highlighting its efficiency in milder weather. The **Full Electric** system shows moderate EUI across all seasons but has a relatively higher EUI compared to **HP and DHW**, especially during **Winter** and **Autumn**.

This comparison highlights the seasonal variations in energy efficiency for different systems and demonstrates that **HP and DHW** is the most efficient solution under the given conditions, particularly in cold regions with varying seasonal demands.

![FIG_7](https://github.com/user-attachments/assets/d1dc75e0-b90d-4c3a-83af-4178b1ec4968)
