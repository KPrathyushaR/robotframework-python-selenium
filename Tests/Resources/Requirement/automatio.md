---
## 1. Testcase Design Rules
---

### 1.1 Business Flow Rules

> - Testcases should contain only business-flow keywords.
> - Login functionality is mandatory for every new testcase.
> - Maximum keywords per testcase: preferably within 7-10 lines.
> - Reuse existing keywords before creating new implementations.
> - Avoid duplicate keyword implementations.
> - Common functionality must be moved into reusable common keywords.
> - Keywords should be modular, maintainable, and preferably within 10–15 lines.
> - Reuse existing CRUD patterns and framework flows.
> - Minimize execution time and improve stability.

---

### 1.2 Documentation Rules

> - Every testcase and keyword must contain documentation.
> - Documentation should not exceed two lines.
> - Documentation must describe actual testcase implementation or methods involved.
> - Do not write generic documentation.
> - Documentation should explain business purpose, main actions performed, and validation involved.


✅ **Correct:**


```robot
[Documentation]    Validates add functionality for Elevator Parameters and verifies successful creation.
```

❌ **Wrong:**

```robot
[Documentation]    This testcase verifies something.
```

---

### 1.3 Validation Rules

> - Validate toast, success, warning, and error messages wherever applicable.
> - Validate expected UI behavior after actions.
> - Prefer dynamic validations over static waits.
> - Validate mandatory field color codes: red (error) before data entry, blue/normal after valid data entry.
> - Validate error margin texts under fields when unique constraints are violated (e.g., "The value must be unique.", "The code must be unique.").
> - Validate Save button enablement only after all mandatory fields are correctly filled.
> - Validate notification messages after CRUD operations (e.g., "ADDED: Domain:", "UPDATED: Parameter category:", "DELETED: Domain:").


---

### 1.4 Wait Rules

> - ❌ Avoid Sleep usage.
> - ✅ Use dynamic waits.
> - 🟡 Use Sleep only if absolutely required.

---
## 2. Locator and Variable Creation Standards
---
### 2.1 General Rules

> - Do not create duplicate locators.
> - Do not create duplicate variables.
> - Search existing framework files before creating new entries.
> - Reuse existing sections whenever available.
> - Create new sections only if no suitable section exists.
---

### 2.2 Locator Rules

> - Maintain locators only in locator files.
> - Group locators by complete functionality/suite.
> - Do not group by buttons, dropdowns, tables, etc.
> - Use common locator sections for shared locators.
> - Maintain alignment and formatting consistency.

✅ **Correct:**

```robot
${DOOR_FAULT_ADD_BUTTON}          //button[text()='Add']
${DOOR_FAULT_SAVE_BUTTON}         //button[text()='Save']
```
❌ **Wrong:**

```robot
${button1}    //button[text()='Add']
```
---

### 2.3 Variable Rules

> - Variables/test data should be maintained only in variable files.
> - Group variables by functionality.
> - Avoid hardcoded values.
> - Ensure test data codes are not already used.
> - Reuse common test data.
---

### 2.4 Section Design Rules

> - All locators and variables belonging to one complete functionality/suite must be maintained under a **single dedicated section**.
> -  Do not split sections by component type.

❌ **Wrong — split by component type:**

```robot
# ELEVATOR - BUTTONS
# ELEVATOR - DROPDOWNS
# ELEVATOR - INPUT FIELDS
```


✅ **Correct — single section per functionality:**


```robot
# =============================================
#  ELEVATOR - PARAMETERS
# =============================================


${ELEVATOR_PARAMETERS_DOMAIN_KCECPU}                        //*[@id="domainName"]/div[2]//*[contains(text(),"KCECPU")]


@{ELEVATOR_PARAMETERS_COLUMN_TEXT}      ${DOMAIN_TEXT}
...                                      ${CODE_TEXT}
...                                      ${PRIORITY_TEXT}
...                                      ${NAME_FAULT_TEXT}
...                                      ${ADD_INFO_TEXT}
...                                      ${DETECTION_TEXT}
...                                      ${OPERATION_TEXT}
...                                      ${RECOVERY_TEXT}
...                                      ${ENGLISH_NAME_TEXT}
...                                      ${REASON_TEXT}
...                                      ${ACTION_TEXT}
...                                      ${SETUP_REQ_TEXT}
...                                      ${MANUAL_RESET_TEXT}
...                                      ${NO_STARTS_TEXT}
...                                      ${SC_OPEN_TEXT}
...                                      ${CHANGE_BOARD_TEXT}
...                                      ${DATAACT_CATEGORY_TEXT}
```


> - All locators for a suite must come under a single section.
> - All variables for a suite must come under a single section.
> - Keep all functionality-related locators together.
> - Reuse the same section for future additions.
> - Avoid creating duplicate functionality sections.


---


## 3. Locator Usage Rules


---


> -  Never use raw locator values inside keywords.
> -  Always use locator variables.
> -  Do not use `Evaluate $TEMPLATE.replace('{}', $VAR)`.
> -  Prefer static locator + filtering approaches.




✅ **Correct:**


```robot
Click Element    ${ADD_BUTTON}
```


❌ **Wrong:**


```robot
Click Element    //button[text()='Add']
```


---


## 4. Testcase Execution Order


---


> Preferred order:
>
> 1. Add
> 2. Edit
> 3. Copy
> 4. Delete
> 5. List View
> 6. Export
> 7. Export With Filter
> 8. Table Settings
> 9. Domain Filtering
> 10. Feature Filtering
> 11. Code Filtering
> 12. Name Filtering
> 13. Description Filtering
> 14. Release Status Filtering
> 15. Created By Filtering
> 16. Created Date Filtering
> 17. Modified By Filtering
> 18. Modified Date Filtering
> 19. View Translation Add
> 20. View Translation Edit
> 21. Page Navigation


> - Maintain ascending order.
> - Insert new testcase in functional sequence.
> - New testcase should be added before Page Navigation if no pattern exists.


---


## 5. Reusable Data and Cleanup Rules


---


### 5.0 Parameter Creation Dependency Chain


> Parameters in KCEDB follow a strict dependency hierarchy. Each level requires the previous level to exist before creation.


**Creation Order for Parameter (mandatory for all targets):**


> 1. **Electrification** — Navigate to Enumerations → Electrifications
>    - Mandatory fields: Value (unique code), Enumeration Name
>    - Non-mandatory: Comment
>    - Add panel elements: Add Electrifications header, Value text, Enumeration Name text, Comment text, error margin texts
>    - Error margin texts: "The value must be unique." (under Value), "The enumeration name cannot be empty." (under Enumeration Name)
>    - Validation: Red color on mandatory fields until filled; changes to normal after valid data entry
>    - Save button enables only when all mandatory fields are valid; if not enabled, values already exist elsewhere
>
> 2. **Domain** — Navigate to Enumerations → Domains
>    - Mandatory fields: Code (unique), Enumeration Name
>    - Non-mandatory: Comment
>    - Dropdowns: Domain Group (target-specific), Electrification (select recently created Enumeration Name from step 1)
>    - Add panel elements: Add Domain header, Code text, Enumeration text, Comment text, Domain Group text, Electrifications text
>    - Error margin text: "The code must be unique." (under Code)
>    - Validation: Red color on Code and Enumeration fields; Domain Group may be auto-set (disabled) for single-target users
>    - Save button enables only when all mandatory fields are valid; if not enabled, code/enumeration values already exist
>
> 3. **Parameter Category** — Navigate to Enumerations → Parameter Categories
>    - Mandatory fields: Code (unique within domain group), Enumeration, Name, Description
>    - Dropdowns: Domain Group (target-specific), Domain (shows "Code + Enumeration" combination from Domains menu)
>    - Add panel elements: Add Parameter Category header, Code text, Enumeration text, Name text, Description text, Domain Group text, Domain text
>    - Error margin text: "Code must be unique in the domain group." (under Code)
>    - Validation: All mandatory fields show red color before data entry; changes to blue/normal after valid data entry
>    - Domain dropdown shows recently created domain (Code with Enumeration combination name)
>    - Save button enables only when all mandatory fields are valid
>
> 4. **Version** (Elevator/Drive/Door/Escalator only) — Navigate to Target → Bindings → Versions
>    - Mandatory fields: Number (format: 00.00.00.00, unique), Name
>    - Non-mandatory: Comment
>    - Add panel elements: Add Version header, Number text, Name text, Comment text
>    - Error margin text: "The number should be unique and adhere to the numeric format: 00.00.00.00" (under Number, appears only after entering value)
>    - Validation: Red color on mandatory fields until filled
>    - Save button enables only when Number and Name are valid
>
> 5. **Product** (Elevator/Drive/Door/Escalator only) — Navigate to Target → Bindings → Products
>    - Mandatory fields: Code (unique), Name
>    - Non-mandatory: Comment
>    - Add panel elements: Add Product header, Code text, Name text, Comment text
>    - Error margin text: "The code must be unique." (under Code)
>    - Validation: Red color on Code and Name fields before data entry; changes to blue/normal after valid data entry
>    - Save button enables only when Code and Name are valid
>
> 6. **Bindings** (Elevator/Drive/Door/Escalator only) — Navigate to Target → Bindings → Add Bindings
>    - Required dropdowns: Product (from step 5), Version (from step 4)
>    - Panel text: "Add bindings to parameters — Select the source binding in order to select parameters which contain it — Select the new bindings which will be added to the selected parameters — The list shows parameters to which the new binding will be added — Start adding by clicking 'Add binding'"
>    - Elements: Source Bindings text, Bindings to be added text
>    - Add Bindings button enables only when both Product and Version are selected from dropdowns
>    - If Product/Version not in list, create them first (steps 4-5)
>
> 7. **Parameter** (target-specific) — Navigate to Target → Parameters
>    - Mandatory fields: Code (unique, greater than zero), Sw Name, English Name, Description, Comment
>    - Required dropdowns: Domain (from step 2), Category (from step 3)
>    - Add panel elements: Add Parameter header, Code text, Sw Name text, English Name text, Description text, Comment text
>    - Error margin text: "The code must be greater than zero and unique in the domain." (under Code)
>    - Validation: All mandatory fields show red color before data entry; changes to blue/normal after valid data entry
>    - Domain dropdown shows recently created domain; Category dropdown shows recently created parameter category
>    - Save button enables only when all mandatory fields are valid


**Creation Order for Fault (all targets):**


> 1. **Electrification** — Same as Parameter chain step 1
> 2. **Domain** — Same as Parameter chain step 2
> 3. **Fault** (target-specific) — Navigate to Target → Faults
>    - Similar to Parameter creation but with fault-specific fields
>    - Required dropdown: Domain (from step 2)
>    - Additional fields vary by target (Priority, Detection, Operation, Recovery, etc.)


**Target-Specific Domain Group Mapping:**


| Target | Domain Group Selection | Bindings Required |
|--------|----------------------|-------------------|
| Elevator | Lift | Yes (Version + Product + Bindings) |
| Drive | Drive | Yes (Version + Product + Bindings) |
| Door | Door | Yes (Version + Product + Bindings) |
| Escalator | Escalator | Yes (Version + Product + Bindings) |
| APM | APM | No |
| Safety | Safety | No |
| Group | Group | No |
| Network | Network | No |
| Monitoring | Monitoring | No |
| Signalization | Signalization | No |


**Rules:**


> - Always create prerequisites before the dependent entity following the numbered order above.
> - Use delete-before-create at each level to ensure idempotent execution.
> - Domain Group dropdown may be disabled (auto-set) for target-specific users; only admin/multi-target users see it enabled.
> - If Save button does not enable after filling fields, the code/enumeration values likely already exist — use unique test data codes.
> - Error margin texts appear under fields when validation fails — check if values are already used in any target.
> - If any field remains red after entering data, the value is invalid or already in use — use a new unique value.
> - The Domain dropdown in Parameter Category shows "Code + Enumeration Name" combination from the Domains menu.
> - For targets requiring Bindings (Elevator, Drive, Door, Escalator), Version and Product must be created before the Parameter.
> - Faults follow a shorter chain (Electrification → Domain → Fault) without needing Parameter Category, Version, Product, or Bindings.


---


### 5.1 Data Reuse


> - Shared suite-level data may be reused.
> - Use delete-before-create for idempotent execution.
> - Reduce duplicate data creation.


---


### 5.2 Cleanup Strategies


---


 **Strategy 1 — Suite-Level Cleanup**


> Shared suite-level data can be created in the Add testcase and reused by remaining testcases (Edit, Copy, Delete, Filtering, Export, Translation).
>
> Example: Add Elevator Parameter creates Domain, Parameter Category, Products, Versions, Bindings.
>
> Cleanup: Delete Elevator Parameter or a designated cleanup testcase removes shared data.


---


 **Strategy 2 — Per-Test Cleanup**


> - Testcase creates its own required data.
> - Testcase removes its own created data.
> - Shared reusable objects (Domain, Parameter Category, Product, Version) may still be reused after Add testcase creation.
>
> Examples: Filtering, List view, Export testcases.


---


 **Strategy 3 — Delete-Before-Create**


> - Delete existing object before creating.
> - Prevent duplicate failures.
> - Ensure idempotent execution.


---


### 5.3 Strategy Selection


> - Shared reusable data →  Strategy 1
> - Independent testcases →  Strategy 2
> - Credential switching / multi-login flows →  Strategy 3


 **Additional rule:** View Translation / Edit Translation testcase may perform cleanup of remaining shared data (Domain, Parameter Category, Products, Versions). This avoids unnecessary login overhead and keeps suite execution efficient.


---


## 6. Module Structure Rules


---


> - Maintain locators in locator files.
> - Maintain variables in variable files.
> - Add all new locators/variables before usage.
> - Multi-module flows must import required resources.
> - Cross-module keywords belong in primary module keyword file.


**Standard module order:**


> 1. Elevator
> 2. Drive
> 3. Group
> 4. LIO
> 5. APM
> 6. Safety
> 7. Escalator
> 8. Door
> 9. Network
> 10. Monitoring
> 11. Non-Kone
> 12. Signalization
> 13. Site
> 14. Localization
> 15. Users
> 16. Enumerations
> 17. Tools


---


## 7. Naming Standards


---


### 7.1 Testcase Naming


> Pattern: `Verify <Action> <Module Name> Functionality`


```
Verify Add Monitoring Fault Functionality
Verify Edit Monitoring Fault Functionality
Verify Delete Monitoring Fault Functionality
```


---


### 7.2 Keyword Naming


```
Add Monitoring Fault
Delete Monitoring Fault
Validate Monitoring Fault Added Successfully
```


---


### 7.3 Keyword Casing


> All keyword calls must use consistent Title Case capitalization.


✅ **Correct:**


```robot
Verify If Product Or Version Is Not Present     ${EVENT_TYPES_MENU}    ${ENUMERATION_VALUE}
Verify Default Input Sections Has Mandatory Fields Highlighted For Events   ${EVENT_CLASS_MENU}
Select Given Target And Click On Given Parameter Menu    ${NETWORK_SIDELINK}    ${NETWORK_FAULTS_MENU}
```


❌ **Wrong:**


```robot
Verify if Product or Version is not present     ${EVENT_TYPES_MENU}    ${ENUMERATION_VALUE}
Verify Default Input sections has Mandatory Fields highlighted for Events   ${EVENT_CLASS_MENU}
Select Given Target and Click on Given Parameter Menu    ${NETWORK_SIDELINK}    ${NETWORK_FAULTS_MENU}
```


> - Every word in a keyword name must start with an uppercase letter (Title Case).
> - Although Robot Framework is case-insensitive, consistent casing improves readability and maintainability.
> - When calling existing keywords, match the defined casing exactly.


---


## 8. AI Agent Rules


---


### 8.1 AI Understanding Rules


> - Rules must contain clear explanations.
> - Combine similar rules in one section.
> - Remove duplicate rules.
> - Keep parent-child relationships for sub-rules.
> - AI should first identify existing implementation before creating new implementation.
> - Existing implementation differences should be analyzed before adding new elements.
> - Do not create duplicate functionality.
> - When a keyword already exists with proper documentation and dynamic waits, do not create a second version with different casing or Sleep-based waits.
> - Before creating any new keyword, search the resource file for existing definitions with the same or similar name (case-insensitive).
> - When fixing keyword issues, verify the keyword is not called from other test suites before modifying or removing it.

### 8.2 Temporary File Cleanup

> - Temporary AI-generated files must not be committed.
> - Remove helper/debug files after execution.
> - Add repeated temporary files into `.gitignore`.
>
> Example: `parse_output*.py
