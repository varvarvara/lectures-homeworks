{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPDM4abJKy59bHjPfXaXoPk",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/varvarvara/lectures-homeworks/blob/master/Lectures/lecture_6/task.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Tz33zLoR1s4b",
        "outputId": "0c73799a-79e8-4ab6-e58c-9c0658d2f12b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a positive integer number: 32\n",
            "Sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269]\n",
            "With cache (1st attempt)): 0.000001 seconds\n",
            "With cache (2nd attempt): 0.000001 seconds\n",
            "Without cache: 0.000005 seconds\n"
          ]
        }
      ],
      "source": [
        "def fibonacci_regular(n: int) -> list:\n",
        "    if n <= 0:\n",
        "        return []\n",
        "    elif n == 1:\n",
        "        return [0]\n",
        "    elif n == 2:\n",
        "        return [0, 1]\n",
        "\n",
        "    s = [0, 1]\n",
        "    fib_1, fib_2 = 0, 1\n",
        "    for i in range(2, n):\n",
        "        fib_1, fib_2 = fib_2, fib_1 + fib_2\n",
        "        s.append(fib_2)\n",
        "    return s\n",
        "\n",
        "import time\n",
        "MY_CACHE: dict[str, str] = {}\n",
        "\n",
        "def fibonacci_cached(n: int) -> list:\n",
        "    if n in MY_CACHE:\n",
        "        return MY_CACHE[n]\n",
        "\n",
        "    if n <= 0:\n",
        "        result = []\n",
        "    elif n == 1:\n",
        "        result = [0]\n",
        "    elif n == 2:\n",
        "        result = [0, 1]\n",
        "    else:\n",
        "        s = [0, 1]\n",
        "        fib_1, fib_2 = 0, 1\n",
        "        for i in range(2, n):\n",
        "            fib_1, fib_2 = fib_2, fib_1 + fib_2\n",
        "            s.append(fib_2)\n",
        "        result = s\n",
        "\n",
        "    MY_CACHE[n] = result\n",
        "    return result\n",
        "\n",
        "\n",
        "try:\n",
        "    n = int(input('Enter a positive integer number: '))\n",
        "    if n <= 0:\n",
        "        print('Error. Enter a positive integer.')\n",
        "    else:\n",
        "        start = time.time() #1st attempt\n",
        "        seq_cached = fibonacci_cached(n)\n",
        "        time_cached = time.time() - start\n",
        "\n",
        "        start = time.time() #2nd attempt\n",
        "        seq_cached = fibonacci_cached(n)\n",
        "        time_cached = time.time() - start\n",
        "\n",
        "        start = time.time()\n",
        "        seq_regular = fibonacci_regular(n)\n",
        "        time_regular = time.time() - start\n",
        "\n",
        "        print(f\"Sequence: {seq_cached}\")\n",
        "        print(f\"With cache (1st attempt)): {time_cached:.6f} seconds\")\n",
        "        print(f\"With cache (2nd attempt): {time_cached:.6f} seconds\")\n",
        "        print(f\"Without cache: {time_regular:.6f} seconds\")\n",
        "\n",
        "except ValueError:\n",
        "    print('Error. Enter a positive integer.')"
      ]
    }
  ]
}