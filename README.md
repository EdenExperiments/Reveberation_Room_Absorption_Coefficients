# BS EN ISO 354:2003 and ISO 9613 results calculator

This is a file which can calculate results based on room conditions and measured reverberation times for BS EN ISO 354:2003, it also includes calculations required to find the power coefficient (m), which uses an attenuation (alpha) from ISO 9613:1993. This program came about due to needing to verify results for an existing excel spreadsheet in a professional acoustic testing environment. To use this for your own results analysis, follow the instructions below.

### Setting Frequency Range

- Finish

### Entering Room Conditions

- Finish

## Further goals

I intend to complete this program with an optional input to ask a user if they wish to calculate a result based on BS EN ISO 11654:1997, to give a single rating value for the absorption properties of the test specimen, providing mean results for the octave bands, 250, 500, 1000, 2000, and 4000 as required by the standard, with an optional 125 Hz octave band result. Then using reference values, calculating the class of the material/system and printing graphs using matplotlib.

Also intend to refactor the code, add in sys.exits(), improve clarity and provide comments on functions 
