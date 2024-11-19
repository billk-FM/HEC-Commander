Depth Damage Functions Charted from the [Go Consequences Occupancy Types JSON](https://github.com/USACE/go-consequences/blob/main/structures/occtypes.json)

More information at the [Go Consequences Wiki](https://github.com/USACE/go-consequences/wiki/Occupancy-Types)

# Building Occupancy Type Charts and Damage Functions

Below are fragility curves organized by occupancy type, displayed at 70% width and centered, along with their corresponding damage functions.

<div align="center">

## Agricultural Occupancy
<img src="AGR1_ddf.png" width="70%">

### AGR1 Damage Functions
| Category   | Function Type   | Source                               | Driver   |
|:-----------|:----------------|:-------------------------------------|:---------|
| Contents   | erosion         | NACCS (CeErNPCn)                     | erosion  |
| Contents   | default         | HEC-FIA damage functions (Galveston) | depth    |
| Contents   | depth           | HEC-FIA damage functions (Galveston) | depth    |
| Structure  | default         | HEC-FIA damage functions (Galveston) | depth    |
| Structure  | erosion         | NACCS (CeErSt)                       | erosion  |
| Structure  | depth           | HEC-FIA damage functions (Galveston) | depth    |

## Apartment Buildings
<img src="APT_ddf.png" width="70%">

### APT Damage Functions
| Category   | Function Type   | Source          | Driver   |
|:-----------|:----------------|:----------------|:---------|
| Contents   | erosion         | NACCS (BhrErCn) | erosion  |
| Structure  | erosion         | NACCS (BhrErSt) | erosion  |

## Commercial Occupancies
<img src="COM_ddf.png" width="70%">

### COM Damage Functions
| Category   | Function Type   | Source           | Driver   |
|:-----------|:----------------|:-----------------|:---------|
| Contents   | erosion         | NACCS (CeErNPCn) | erosion  |
| Structure  | erosion         | NACCS (CeErSt)   | erosion  |

<img src="COM1_ddf.png" width="70%">

### COM1 Damage Functions
| Category   | Function Type   | Source                                          | Driver   |
|:-----------|:----------------|:------------------------------------------------|:---------|
| Contents   | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | erosion         | NACCS (CeErNPCn)                                | erosion  |
| Contents   | depth, salinity | NACCS combined curves for commercial structures | depth    |
| Structure  | salinity, depth | NACCS combined curves for commercial structures | depth    |
| Structure  | erosion         | NACCS (CeErSt)                                  | erosion  |
| Structure  | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | depth           | HEC-FIA damage functions (Galveston)            | depth    |

<img src="COM2_ddf.png" width="70%">

### COM2 Damage Functions
| Category   | Function Type   | Source                                          | Driver   |
|:-----------|:----------------|:------------------------------------------------|:---------|
| Contents   | erosion         | NACCS (CeErNPCn)                                | erosion  |
| Contents   | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | depth, salinity | NACCS combined curves for commercial structures | depth    |
| Contents   | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | salinity, depth | NACCS combined curves for commercial structures | depth    |
| Structure  | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | erosion         | NACCS (CeErSt)                                  | erosion  |

<img src="COM3_ddf.png" width="70%">

### COM3 Damage Functions
| Category   | Function Type   | Source                                          | Driver   |
|:-----------|:----------------|:------------------------------------------------|:---------|
| Contents   | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | depth, salinity | NACCS combined curves for commercial structures | depth    |
| Contents   | erosion         | NACCS (CeErNPCn)                                | erosion  |
| Structure  | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | depth, salinity | NACCS combined curves for commercial structures | depth    |
| Structure  | erosion         | NACCS (CeErSt)                                  | erosion  |
| Structure  | default         | HEC-FIA damage functions (Galveston)            | depth    |

<img src="COM4_ddf.png" width="70%">

### COM4 Damage Functions
| Category   | Function Type   | Source                                          | Driver   |
|:-----------|:----------------|:------------------------------------------------|:---------|
| Contents   | salinity, depth | NACCS combined curves for commercial structures | depth    |
| Contents   | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | erosion         | NACCS (CeErNPCn)                                | erosion  |
| Contents   | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | salinity, depth | NACCS combined curves for commercial structures | depth    |
| Structure  | erosion         | NACCS (CeErSt)                                  | erosion  |
| Structure  | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | depth           | HEC-FIA damage functions (Galveston)            | depth    |

<img src="COM5_ddf.png" width="70%">

### COM5 Damage Functions
| Category   | Function Type   | Source                                          | Driver   |
|:-----------|:----------------|:------------------------------------------------|:---------|
| Contents   | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | salinity, depth | NACCS combined curves for commercial structures | depth    |
| Contents   | erosion         | NACCS (CeErNPCn)                                | erosion  |
| Structure  | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | depth, salinity | NACCS combined curves for commercial structures | depth    |
| Structure  | erosion         | NACCS (CeErSt)                                  | erosion  |

<img src="COM6_ddf.png" width="70%">

### COM6 Damage Functions
| Category   | Function Type   | Source                                          | Driver   |
|:-----------|:----------------|:------------------------------------------------|:---------|
| Contents   | depth, salinity | NACCS combined curves for commercial structures | depth    |
| Contents   | erosion         | NACCS (BhrErCn)                                 | erosion  |
| Contents   | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | salinity, depth | NACCS combined curves for commercial structures | depth    |
| Structure  | erosion         | NACCS (BhrErSt)                                 | erosion  |

<img src="COM7_ddf.png" width="70%">

### COM7 Damage Functions
| Category   | Function Type   | Source                                          | Driver   |
|:-----------|:----------------|:------------------------------------------------|:---------|
| Contents   | salinity, depth | NACCS combined curves for commercial structures | depth    |
| Contents   | erosion         | NACCS (CeErNPCn)                                | erosion  |
| Contents   | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | depth, salinity | NACCS combined curves for commercial structures | depth    |
| Structure  | erosion         | NACCS (CeErSt)                                  | erosion  |

<img src="COM8_ddf.png" width="70%">

### COM8 Damage Functions
| Category   | Function Type   | Source                                          | Driver   |
|:-----------|:----------------|:------------------------------------------------|:---------|
| Contents   | erosion         | NACCS (CeErNPCn)                                | erosion  |
| Contents   | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | salinity, depth | NACCS combined curves for commercial structures | depth    |
| Structure  | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | salinity, depth | NACCS combined curves for commercial structures | depth    |
| Structure  | erosion         | NACCS (CeErSt)                                  | erosion  |

<img src="COM9_ddf.png" width="70%">

### COM9 Damage Functions
| Category   | Function Type   | Source                                          | Driver   |
|:-----------|:----------------|:------------------------------------------------|:---------|
| Contents   | depth, salinity | NACCS combined curves for commercial structures | depth    |
| Contents   | erosion         | NACCS (CeErNPCn)                                | erosion  |
| Contents   | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | salinity, depth | NACCS combined curves for commercial structures | depth    |
| Structure  | erosion         | NACCS (CeErSt)                                  | erosion  |

<img src="COM10_ddf.png" width="70%">

### COM10 Damage Functions
| Category   | Function Type   | Source                                          | Driver   |
|:-----------|:----------------|:------------------------------------------------|:---------|
| Contents   | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Contents   | salinity, depth | NACCS combined curves for commercial structures | depth    |
| Structure  | default         | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | depth           | HEC-FIA damage functions (Galveston)            | depth    |
| Structure  | salinity, depth | NACCS combined curves for commercial structures | depth    |

## Educational Occupancies
<img src="EDU1_ddf.png" width="70%">

### EDU1 Damage Functions
| Category   | Function Type   | Source                               | Driver   |
|:-----------|:----------------|:-------------------------------------|:---------|
| Contents   | default         | HEC-FIA damage functions (Galveston) | depth    |
| Contents   | depth           | HEC-FIA damage functions (Galveston) | depth    |
| Contents   | erosion         | NACCS (CeErNPCn)                     | erosion  |
| Structure  | erosion         | NACCS (CeErSt)                       | erosion  |
| Structure  | default         | HEC-FIA damage functions (Galveston) | depth    |
| Structure  | depth           | HEC-FIA damage functions (Galveston) | depth    |

<img src="EDU2_ddf.png" width="70%">

### EDU2 Damage Functions
| Category   | Function Type   | Source                               | Driver   |
|:-----------|:----------------|:-------------------------------------|:---------|
| Contents   | default         | HEC-FIA damage functions (Galveston) | depth    |
| Contents   | depth           | HEC-FIA damage functions (Galveston) | depth    |
| Structure  | default         | HEC-FIA damage functions (Galveston) | depth    |
| Structure  | depth           | HEC-FIA damage functions (Galveston) | depth    |

## Government Buildings
<img src="GOV1_ddf.png" width="70%">

### GOV1 Damage Functions
| Category   | Function Type   | Source                               | Driver   |
|:-----------|:----------------|:-------------------------------------|:---------|
| Contents   | default         | HEC-FIA damage functions (Galveston) | depth    |
| Contents   | depth           | HEC-FIA damage functions (Galveston) | depth    |
| Contents   | erosion         | NACCS (CeErNPCn)                     | erosion  |
| Structure  | default         | HEC-FIA damage functions (Galveston) | depth    |
| Structure  | depth           | HEC-FIA damage functions (Galveston) | depth    |
| Structure  | erosion         | NACCS (CeErSt)                       | erosion  |

<img src="GOV2_ddf.png" width="70%">

### GOV2 Damage Functions
| Category   | Function Type   | Source                               | Driver   |
|:-----------|:----------------|:-------------------------------------|:---------|
| Contents   | default         | HEC-FIA damage functions (Galveston) | depth    |
| Contents   | depth           | HEC-FIA damage functions (Galveston) | depth    |
| Contents   | erosion         | NACCS (CeErNPCn)                     | erosion  |
| Structure  | default         | HEC-FIA damage functions (Galveston) | depth    |
| Structure  | depth           | HEC-FIA damage functions (Galveston) | depth    |
| Structure  | erosion         | NACCS (CeErSt)                       | erosion  |

## High Occupancy Buildings
<img src="HIGH_ddf.png" width="70%">

### HIGH Damage Functions
| Category   | Function Type   | Source          | Driver   |
|:-----------|:----------------|:----------------|:---------|
| Contents   | erosion         | NACCS (BhrErCn) | erosion  |
| Structure  | erosion         | NACCS (BhrErSt) | erosion  |









# Python Code Used to Generate this Page:
AI-Generated, use at your own caution!

Just point the script below at the location of occtypes.json on your local machine, and you can re-create the plots above. 



### Load C:\GH\go-consequences_win\structures\occtypes.json and convert to DataFrame
```
import json
import pandas as pd

with open(r"structures/occtypes.json", "r") as file:
    structure_types = json.load(file)

# Create lists to store the flattened data
rows = []
for key, value in structure_types.items():
    if isinstance(value, dict):
        for subkey, details in value.items():
            if isinstance(details, dict):
                for detail_key, detail_value in details.items():
                    rows.append({
                        'Type': key,
                        'Subtype': subkey,
                        'Detail': detail_key,
                        'Value': detail_value
                    })
            else:
                rows.append({
                    'Type': key,
                    'Subtype': subkey,
                    'Detail': 'name',
                    'Value': details
                })

# Create DataFrame
df = pd.DataFrame(rows)
display(df)



# Filter for RES1-1SNB damage functions and display details
res1_snb_df = df[(df['Subtype'] == 'RES1-1SNB') & (df['Detail'] == 'componentdamagefunctions')]

if not res1_snb_df.empty:
    # Get the damage functions dictionary
    damage_funcs = res1_snb_df.iloc[0]['Value']
    
    print("\nRES1-1SNB Component Damage Functions:")
    print(json.dumps(damage_funcs, indent=2))
else:
    print("\nNo damage functions found for RES1-1SNB")
```

### Print DDF Information about Each Occupancy Type 
```
# Get all occupancy types with damage functions
damage_funcs_df = df[df['Detail'] == 'componentdamagefunctions']

# Iterate through each occupancy type
for _, row in damage_funcs_df.iterrows():
    damage_funcs = row['Value']
    table_rows = []
    
    # Print occupancy type header
    print(f"\n## {row['Subtype']}")
    
    # Process contents damage functions
    if 'contents' in damage_funcs and 'damagefunctions' in damage_funcs['contents']:
        for func_type, func_details in damage_funcs['contents']['damagefunctions'].items():
            table_rows.append({
                'Category': 'Contents',
                'Function Type': func_type,
                'Source': func_details.get('source', ''),
                'Driver': func_details.get('damagedriver', '')
            })
            
    # Process structure damage functions        
    if 'structure' in damage_funcs and 'damagefunctions' in damage_funcs['structure']:
        for func_type, func_details in damage_funcs['structure']['damagefunctions'].items():
            table_rows.append({
                'Category': 'Structure', 
                'Function Type': func_type,
                'Source': func_details.get('source', ''),
                'Driver': func_details.get('damagedriver', '')
            })

    # Create DataFrame and display as markdown table for this occupancy type
    if table_rows:
        table_df = pd.DataFrame(table_rows).drop_duplicates()
        print(table_df.to_markdown(index=False))
    else:
        print("No damage functions defined")
```

### Plot all DDF Distributions:
```
def plot_all_distributions(data):
    """
    Create comprehensive plots for COM3 showing all distribution types and their uncertainties
    """
    com3_funcs = data['occupancytypes']['COM3']['componentdamagefunctions']
    
    # Create figure with 3 subplots (one for each distribution type)
    fig, (ax_det, ax_tri, ax_emp) = plt.subplots(3, 1, figsize=(12, 15))
    
    # Colors for consistent plotting
    colors = {'contents': 'blue', 'structure': 'red'}
    
    # 1. Plot Deterministic Distributions (depth damage)
    ax_det.set_title('Deterministic Distributions (Depth Damage)', fontsize=12)
    for component in ['contents', 'structure']:
        if 'depth' in com3_funcs[component]['damagefunctions']:
            func_data = com3_funcs[component]['damagefunctions']['depth']
            x_vals = func_data['damagefunction']['xvalues']
            y_vals = [y['parameters']['value'] for y in func_data['damagefunction']['ydistributions']]
            ax_det.plot(x_vals, y_vals, 
                       label=f"{component.title()} ({func_data['source']})",
                       color=colors[component])
    
    # 2. Plot Triangular Distributions (erosion damage)
    ax_tri.set_title('Triangular Distributions (Erosion Damage)', fontsize=12)
    for component in ['contents', 'structure']:
        if 'erosion' in com3_funcs[component]['damagefunctions']:
            func_data = com3_funcs[component]['damagefunctions']['erosion']
            x_vals = func_data['damagefunction']['xvalues']
            
            # Get min, most likely, and max values
            y_likely = []
            y_min = []
            y_max = []
            for y in func_data['damagefunction']['ydistributions']:
                params = y['parameters']
                y_likely.append(params['mostlikely'] * 100)
                y_min.append(params['min'] * 100)
                y_max.append(params['max'] * 100)
            
            # Plot most likely line and uncertainty band
            ax_tri.plot(x_vals, y_likely, 
                       label=f"{component.title()} ({func_data['source']})",
                       color=colors[component])
            ax_tri.fill_between(x_vals, y_min, y_max, 
                              color=colors[component], alpha=0.2)
    
    # 3. Plot Empirical Distributions (depth, salinity damage)
    ax_emp.set_title('Empirical Distributions (Depth with Salinity)', fontsize=12)
    for component in ['contents', 'structure']:
        if 'depth, salinity' in com3_funcs[component]['damagefunctions']:
            func_data = com3_funcs[component]['damagefunctions']['depth, salinity']
            x_vals = func_data['damagefunction']['xvalues']
            
            # For empirical, plot min values and indicate distribution range
            y_vals = []
            y_max = []
            for y in func_data['damagefunction']['ydistributions']:
                if y['type'] == 'EmpiricalDistribution':
                    params = y['parameters']
                    y_vals.append(params['minvalue'])
                    y_max.append(params['maxvalue'])
                elif y['type'] == 'DeterministicDistribution':
                    y_vals.append(y['parameters']['value'])
                    y_max.append(y['parameters']['value'])
            
            ax_emp.plot(x_vals, y_vals, 
                       label=f"{component.title()} Min ({func_data['source']})",
                       color=colors[component])
            ax_emp.fill_between(x_vals, y_vals, y_max,
                              color=colors[component], alpha=0.2,
                              label=f"{component.title()} Range")
    
    # Customize all plots
    for ax in [ax_det, ax_tri, ax_emp]:
        ax.set_xlabel("Depth/Erosion (%)")
        ax.set_ylabel('Damage (%)')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(loc='lower right')
        ax.set_ylim(0, 100)
    
    # Update x-label for depth plots
    ax_det.set_xlabel("Depth (ft)")
    ax_emp.set_xlabel("Depth (ft)")
    
    plt.tight_layout()
    plt.show()

# Load and plot
with open(r"structures\occtypes.json", "r") as file:
    data = json.load(file)
    
plot_all_distributions(data)
```

