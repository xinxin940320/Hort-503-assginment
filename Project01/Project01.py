"""A Python script that performs simple read trimming of a FASTQ file.

.. module:: Project01
   :platform: Unix, Windows
   :synopsis: This script receives as input a FASTQ file and a set of arguments
      that control trimming. A new FASTQ file is generated containing only
      trimmed reads that meet the given requirements.

.. moduleauthor:: ENTER YOUR NAME HERE

"""

from sys import argv

def get_read(fq):


    """Extract a single read from a FASTQ file.

    Reads in a FASTQ file are stored in 4 lines that contain the
    sequence_id, nucleotide sequence, a second id, and a series of
    characters represeting quality scores.

    :param fq: A file handle for the FASTQ file
    :type fq: An io.TextIOBase object (created using the open() function).

    :return: a list containing 4 strings: the sequence ID, nucleotide sequence,
        second ID, and the quality score sequence. If there are no more
        sequences in the FASTQ file then this function returns False.
    :rtype: a list with four elements
    """
    seq_id = fq.readline().strip()
    seq = fq.readline().strip()
    second_id = fq.readline().strip()
    seq_score = fq.readline().strip()

    if not seq_id:
        return False

    else:
        return(seq_id, seq, second_id, seq_score)

print(argv)




def trim_read_front(read, min_score, min_size):

    """Trims the low quality nucleotides from the front of a reads' sequences.

    This function examines the quality score of each nucleotide sequence
    starting from the first position of the sequence. When it encouters a
    high quality score it stops trimming and returns an updated read.

    :param read: A list containing for elements in this order: the sequence ID,
        the nucleotide sequence string, a secondary identifier string, and a
        quality score string.
    :type read: a list

    :param min_q:  The minimum quality score that a nucleotide must have to
        not be trimmed (e.g. 20).
    :type min_q:  integer

    :param min_size:  The minimum size that the sequence must have after
        trimming to keep the read (e.g. 25).
    :type min_size: integer

    :return: a list just like the the get_read() function returns but with the
       low-quality reads (and corresponding quality scores) trimmed off the
       front of the string. If the remaining trimmed read is smaller than the
       desired minimum read length then this function returns False.
    :rtype: a list with four elements
    """
    seq_id, seq, second_id, seq_score = read

    # numb_scores = []
    # for n in seq_score:
        # numb_scores.append(ord(n) - 33)

    numb_scores = [ord(n) - 33 for n in seq_score]
    trim_index = 0
    for m in numb_scores:
        if m < min_score:
            trim_index += 1
        else:
            break
    trimmed_sequence = seq[trim_index:]
    trimmed_scores = seq_score[trim_index:]
    if len(trimmed_sequence) >= min_size:
        return [seq_id, trimmed_sequence, second_id, trimmed_scores]
    else:
        return False

#
# The main function for the script.
#
def main(argv):
    """The main function of this script.

    After trimming is completed, the fucntion prints out three status lines. The
    first indicates the total number of reads that were found. The second
    indicates how many reads were removed for being too short after trimming and
    the third indicates how many reas were trimmed and kept.

    The script will create a new FASTQ file of just the trimmed reads and name
    it according to the argument provided by the user when running the script.

    :param argv:  The incoming arguments to this script as
       provided by the sys.argv variable.  There must be four total arguments
       provid ed to the script must be in the following order

       - The filename for the input FASTQ file
       - The filename for the new output FASTQ file that this script creates
       - An integer for the minimum quality score. Anything below this at the
         beginning of each read's nucleotide sequence is trimmed off.
       - An integer indicating how large a read's nucleotide sequence must
         be after trimming in order to keep it.
    """
    Script, input_file, out_file, min_score, min_size = argv
    min_score = int(min_score)
    min_size = int(min_size)
    count_total = 0
    count_removed = 0
    count_trimmed = 0
    with open (input_file, "r") as file_handle:
        with open (out_file, "w") as output_file:

            read = get_read(file_handle)
            while read:
                count_total += 1
                trim = trim_read_front(read, min_score, min_size)
                if trim:
                    raw_seq = read [1]
                    trim_seq = trim [1]
                    if raw_seq != trim_seq:
                        count_trimmed += 1
                    output_file.write("\n".join(trim) + "\n")
                else:
                    count_removed +=1

                # seq_id, trimmed_sequence, second_id, trimmed_scores = trim
                read = get_read(file_handle)

    print(f"{count_total} reads were found.")
    print(f"{count_removed} reads were removed.")
    print(f"{count_trimmed} reads were trimmed.")
    print("Done.")


# Begin the program by calling the main function.
main(argv)
