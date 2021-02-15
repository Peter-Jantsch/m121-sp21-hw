test = {
  'name': 'q2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> player_names.num_columns
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> player_names.num_rows
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure that you have the correct column labels!;
          >>> np.asarray(player_names.labels).item(1) != "name identity"
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure that you have the correct column labels!;
          >>> np.asarray(player_names.labels).item(1) == "Players"
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
